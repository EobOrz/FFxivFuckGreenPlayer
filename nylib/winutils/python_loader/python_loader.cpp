#include <stddef.h>
#include <stdexcept>
#include <windows.h>
#include <format>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <locale>
#include <codecvt>

#define _errV_(x, ...) (std::runtime_error(std::format(x "(at {}:{})", __VA_ARGS__, __FILE__, __LINE__)))
#define _err_(x) (std::runtime_error(std::format(x "(at {}:{})", __FILE__, __LINE__)))
#define _throwV_(x, ...)              \
    {                                 \
        throw _errV_(x, __VA_ARGS__); \
    }
#define _throw_(x)      \
    {                   \
        throw _err_(x); \
    }

typedef struct
{
    WCHAR *pyDll;
    WCHAR *pyMain;
    WCHAR *pyPaths;
} PyLoaderConfig;
PyLoaderConfig *g_cfg = NULL;

void GetSomeProcAddress(HMODULE hModule, const char **names, void **funcs)
{
    for (size_t i = 0; names[i]; i++)
    {
        funcs[i] = GetProcAddress(hModule, names[i]);
        if (funcs[i] == NULL)
        {
            _throwV_("Failed to get {}, GetLastError: {}", names[i], GetLastError());
        }
    }
}

std::string wcharToString(const WCHAR * wcharArray) {
    try {
        std::wstring wstr(wcharArray);
        std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>> converter;
        return converter.to_bytes(wstr);
    } catch (const std::range_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return "";
    }
}

std::string ReadFile(WCHAR *filePath)
{
    std::ifstream file(filePath);
    if (!file.is_open())
    {
        _throwV_("Failed to open file: {}", wcharToString(filePath));
    }
    std::ostringstream ss;
    ss << file.rdbuf();
    return ss.str();
}

void __LoadPython()
{
    if (g_cfg == NULL)
    {
        _throw_("cfg is NULL");
    }
    {
        AllocConsole();
        freopen("CONOUT$", "w", stdout);
        freopen("CONOUT$", "w", stderr);
        freopen("CONIN$", "r", stdin);
    }
    HMODULE hModule = LoadLibraryW(g_cfg->pyDll);
    if (hModule == NULL)
    {
        _throwV_("Failed to load python dll: {} GetLastError: {}", wcharToString(g_cfg->pyDll), GetLastError());
    }

    static const char *funcNames[] = {"Py_Initialize", "Py_Finalize", "PyRun_SimpleFile", "PyRun_SimpleString", NULL};
    void *funcs[4];
    try
    {
        GetSomeProcAddress(hModule, funcNames, funcs);
    }
    catch (std::exception &e)
    {
        FreeLibrary(hModule);
        throw e;
    }
    auto Py_Initialize = (void (*)())funcs[0];
    auto Py_Finalize = (void (*)())funcs[1];
    auto PyRun_SimpleFile = (void (*)(FILE *, const char *))funcs[2];
    auto PyRun_SimpleString = (void (*)(const char *))funcs[3];

    std::string script;
    try
    {
        script = ReadFile(g_cfg->pyMain);
    }
    catch (std::exception &e)
    {
        FreeLibrary(hModule);
        throw e;
    }
    std::string s_pyMain = wcharToString(g_cfg->pyMain), s_pyPaths = wcharToString(g_cfg->pyPaths);
    std::string initCode = std::format(
        "import sys\n"
        "import io\n"
        "import os.path\n"
        "__file__ = r\"{}\"\n"
        "sys.stderr = sys.stdout = io.open(\"CONOUT$\", \"wt\", encoding=\"utf-8\")\n"
        "def parse_path(paths):\n"
        "    if isinstance(paths, str):\n"
        "        paths = paths.split(os.pathsep)\n"
        "    for path in paths:\n"
        "        if path and path not in sys.path:\n"
        "            sys.path.append(path)\n"
        "parse_path(r\"{}\")\n"
        "parse_path(os.path.dirname(__file__))\n",
        s_pyMain, s_pyPaths);

    Py_Initialize();
    PyRun_SimpleString(initCode.c_str());
    PyRun_SimpleString(script.c_str());
    Py_Finalize();

    FreeLibrary(hModule);
}

ULONG WINAPI _LoadPython()
{
    try
    {
        __LoadPython();
    }
    catch (std::exception &e)
    {
        std::cerr << e.what() << std::endl;
    }
    return 0;
}

extern "C" __declspec(dllexport) void LoadPython(PyLoaderConfig *cfg)
{
    g_cfg = cfg;
    _LoadPython();
    // CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)_LoadPython, NULL, 0, NULL);
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD dwReason, PVOID pvReserved)
{
    switch (dwReason)
    {
    case DLL_PROCESS_ATTACH:
        break;
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}
