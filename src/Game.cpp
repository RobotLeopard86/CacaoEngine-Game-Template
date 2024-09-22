#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#include "Cacao.hpp"

extern "C" {
    EXPORT void _CacaoLaunch() {
        Cacao::Logging::ClientLog("Hi!");
        Cacao::WorldManager::GetInstance()->CreateWorld<Cacao::PerspectiveCamera>("World");
        Cacao::WorldManager::GetInstance()->SetActiveWorld("World");
    }

    EXPORT void _CacaoExiting() {
        Cacao::Logging::ClientLog("Bye!");
    }
}
