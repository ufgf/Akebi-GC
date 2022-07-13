#include "pch-il2cpp.h"
#include "main.h"

#include <helpers.h>
#include <il2cpp-init.h>
#include <cheat/cheat.h>
#include <cheat-base/cheat/misc/Settings.h>

#include <tlhelp32.h>
#include <cheat/ILPatternScanner.h>
#include <resource.h>
#include <cheat/debugger.h>

void Run(HMODULE* phModule)
{
	ResourceLoader::SetModuleHandle(*phModule);
	
	auto cheatDir = std::filesystem::path(util::GetModulePath(*phModule)).parent_path();

	// Init config
	config::Initialize((cheatDir / "cfg.json").string());

	// Init logger
	auto& settings = cheat::feature::Settings::GetInstance();
	if (settings.f_FileLogging)
	{
		Logger::PrepareFileLogging((cheatDir / "logs").string());
		Logger::SetLevel(Logger::Level::Trace, Logger::LoggerType::FileLogger);
	}

	if (settings.f_ConsoleLogging)
	{
		Logger::SetLevel(Logger::Level::Debug, Logger::LoggerType::ConsoleLogger);
		il2cppi_new_console();
	}

	DebuggerBypassPre();

	while (GetModuleHandle("UserAssembly.dll") == nullptr)
	{
		LOG_DEBUG("UserAssembly.dll isn't initialized, waiting for 2 sec.");
		Sleep(2000);
	}

#ifdef _DEBUG
	LOG_DEBUG("Waiting 10sec for loading game library.");
	Sleep(15000);
#else
	LOG_DEBUG("Waiting 15sec for game initialize.");
    Sleep(15000);
#endif
	
	DebuggerBypassPost();

	init_il2cpp();

	cheat::Init();

    LOG_DEBUG("Config path is at %s", (cheatDir / "cfg.json").string().c_str());
}