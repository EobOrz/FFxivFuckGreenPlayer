#include <windows.h>
#include <winternl.h>
#include <Shlwapi.h>
#include <stdio.h>
// #include <Python.h>

#pragma comment( lib, "Shlwapi.lib")
#pragma comment( lib, "user32.lib")

static HMODULE hOrig = NULL;
static HANDLE hThread = NULL;
static WCHAR pyDll[MAX_PATH] = { 0 };
static WCHAR pyMain[MAX_PATH] = { 0 };

#define HANDLE_ERROR(msg, ...) { \
    WCHAR buffer[1024]; \
    swprintf(buffer, 1024, L"Line:%d " msg, __LINE__, __VA_ARGS__); \
    MessageBoxW(NULL, buffer, L"Error", MB_ICONERROR); \
    return 1; \
}

// Code Gen Start
#define DEFAULT_ORIG L"/*REPLACE_ORIG_DLL_HERE*/"
#define DEFAULT_PYDLL L"/*REPLACE_PY_DLL_HERE*/"
#define DEFAULT_PYMAIN L"/*REPLACE_PY_MAIN_HERE*/"


/*REPLACE_DEF_EXPORT_HERE*/

ULONG WINAPI InitHijack()
{
/*REPLACE_SET_EXPORT_HERE*/
return 0;
}
// Code Gen End

ULONG WINAPI GetCfgValue(LPCWSTR sect, LPCWSTR key, LPWSTR value, DWORD maxLen)
{

    static WCHAR path[MAX_PATH] = { 0 };
	if (path[0] == 0)
	{
        GetModuleFileNameW(NULL, path, MAX_PATH);
        PathRemoveFileSpecW(path);
		PathCombineW(path, path, L"pyHijack.ini");
	}
	if (PathFileExistsW(path) == FALSE)
	{
		return 0;
	}
	return GetPrivateProfileStringW(sect, key, L"", value, maxLen, path);
}

size_t FileSize(FILE* fp)
{
    size_t push = ftell(fp);
    fseek(fp, 0, SEEK_END);
    size_t fileSize = ftell(fp);
    fseek(fp, push, SEEK_SET);
    return fileSize;
}

ULONG WINAPI RunPython()
{
	DWORD err = 0;
	HMODULE hModule = LoadLibraryW(pyDll);
	if (hModule == NULL)
	{
        HANDLE_ERROR(L"LoadLibraryW(%ws) failed: %d" ,pyDll , GetLastError());
	}

	typedef void(*Py_Initialize_t)();
	Py_Initialize_t Py_Initialize = (Py_Initialize_t)GetProcAddress(hModule, "Py_Initialize");
	if (Py_Initialize == NULL)
	{
        FreeLibrary(hModule);
        HANDLE_ERROR(L"GetProcAddress(Py_Initialize) failed: %d", GetLastError());
	}

	typedef void(*Py_Finalize_t)();
	Py_Finalize_t Py_Finalize = (Py_Finalize_t)GetProcAddress(hModule, "Py_Finalize");
	if (Py_Finalize == NULL)
	{
        FreeLibrary(hModule);
        HANDLE_ERROR(L"GetProcAddress(Py_Finalize) failed: %d", GetLastError());
	}

	typedef void(*PyRun_SimpleFile_t)(FILE* fp, const char* filename);
	PyRun_SimpleFile_t PyRun_SimpleFile = (PyRun_SimpleFile_t)GetProcAddress(hModule, "PyRun_SimpleFile");
	if (PyRun_SimpleFile == NULL)
	{
        FreeLibrary(hModule);
        HANDLE_ERROR(L"GetProcAddress(PyRun_SimpleFile) failed: %d", GetLastError());
	}

	typedef void(*PyRun_SimpleString_t)(const char* code);
	PyRun_SimpleString_t PyRun_SimpleString = (PyRun_SimpleString_t)GetProcAddress(hModule, "PyRun_SimpleString");
	if (PyRun_SimpleString == NULL)
    {
        FreeLibrary(hModule);
        HANDLE_ERROR(L"GetProcAddress(PyRun_SimpleString) failed: %d", GetLastError());
    }

	FILE* fp;
	if (err = _wfopen_s(&fp, pyMain, L"r"))
	{
		FreeLibrary(hModule);
        HANDLE_ERROR(L"_wfopen_s(%ws) failed: %d", pyMain, err);
	}

	size_t fileSize = FileSize(fp);
	char* mainBuffer = (char*)malloc(fileSize + 1);
    mainBuffer[fread(mainBuffer, 1, fileSize, fp)] = 0;

    static char initTemplate[] =
    "import sys\n"
    "import io\n"
    "import os.path\n"
    "__file__ = r\"%ws\"\n"
    "sys.stderr = sys.stdout = io.open(\"CONOUT$\", \"wt\", encoding=\"utf-8\")\n"
    "def parse_path(paths):\n"
    "    if isinstance(paths, str):\n"
    "        paths = paths.split(os.pathsep)\n"
    "    for path in paths:\n"
    "        if path and path not in sys.path:\n"
    "            sys.path.append(path)\n"
    "parse_path(r\"%ws\")\n"
    "parse_path(os.path.dirname(__file__))\n";

    WCHAR mainDir[MAX_PATH] = { 0 };
    memcpy(mainDir, pyMain, sizeof(mainDir));
    PathRemoveFileSpecW(mainDir);

    WCHAR cfgPath[2048] = { 0 };
    GetCfgValue(L"Python", L"path", cfgPath, sizeof(cfgPath));

    char* initBuffer = (char*)malloc(snprintf(NULL, 0, initTemplate, pyMain, cfgPath) + 1);
    initBuffer[sprintf(initBuffer, initTemplate, pyMain, cfgPath)] = 0;
	fclose(fp);

	Py_Initialize();
	PyRun_SimpleString(initBuffer);
	PyRun_SimpleString(mainBuffer);
	Py_Finalize();

	free(initBuffer);
	free(mainBuffer);
	return 0;
}

ULONG WINAPI Init()
{
    DisableThreadLibraryCalls(hOrig);
    WCHAR buffer[MAX_PATH] = { 0 };

    if (GetCfgValue(L"Hijack", L"orig", buffer, MAX_PATH) == 0)
    {
        memcpy(buffer, DEFAULT_ORIG, sizeof(DEFAULT_ORIG));
    }

    if (PathFileExistsW(buffer) == FALSE)
    {
        HANDLE_ERROR(L"orig dll not found: %ws", buffer);
    }

    hOrig = LoadLibraryW(buffer);
    if (hOrig == NULL)
    {
        HANDLE_ERROR(L"LoadLibraryW(%ws) failed: %d", buffer, GetLastError());
    }

    if (GetCfgValue(L"Hijack", L"python_dll", pyDll, MAX_PATH) == 0)
    {
        memcpy(pyDll, DEFAULT_PYDLL, sizeof(DEFAULT_PYDLL));
    }

    if (PathFileExistsW(pyDll) == FALSE)
    {
        HANDLE_ERROR(L"python dll not found: %ws", pyDll);
    }

    if (GetCfgValue(L"Hijack", L"python_main", pyMain, MAX_PATH) == 0)
    {
        memcpy(pyMain, DEFAULT_PYMAIN, sizeof(DEFAULT_PYMAIN));
    }

    if (PathFileExistsW(pyMain) == FALSE)
    {
        HANDLE_ERROR(L"python main not found: %ws", pyMain);
    }

    if (GetCfgValue(L"Hijack", L"create_console", buffer, MAX_PATH))
    {
        AllocConsole();
        FILE* fp;
        freopen_s(&fp, "CONOUT$", "w", stdout);
        freopen_s(&fp, "CONOUT$", "w", stderr);
        freopen_s(&fp, "CONIN$", "r", stdin);
    }

    if (InitHijack())
    {
        return 1;
    }

    hThread = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)RunPython, NULL, 0, NULL);
    if (hThread == NULL)
    {
        HANDLE_ERROR(L"CreateThread failed: %d", GetLastError());
    }


    return 0;
}


BOOL APIENTRY DllMain(HMODULE hModule, DWORD dwReason, PVOID pvReserved)
{
	if (dwReason == DLL_PROCESS_ATTACH)
	{
		if (Init())
        {
            return FALSE;
        }
	}
	else if (dwReason == DLL_PROCESS_DETACH)
	{
        if (hOrig)
        {
            FreeLibrary(hOrig);
        }
	}

	return TRUE;
}
