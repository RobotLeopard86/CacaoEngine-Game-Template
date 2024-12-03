project('cacao-engine-template', 'cpp', default_options: ['cpp_std=c++20'])

cacao = subproject('cacaoengine', required: true, default_options: ['use_backend=gl-glfw', 'build_playground=false', 'exe_name=cacao-template'])
cacao_dep = cacao.get_variable('cacao_dep')

launch = shared_module('launch', name_prefix: '', dependencies: cacao_dep, sources: [
	'src/Game.cpp'
], build_by_default: true)

cacao_exe = cacao.get_variable('cacao_exe')
python = find_program('python', required: true)
run_target('bundle', command: [python, meson.project_source_root()/'scripts'/'bundle.py'], depends: [
	launch,
	cacao_exe
])
run_target('run', command: [python, meson.project_source_root()/'scripts'/'bundleandrun.py'], depends: [
	launch,
	cacao_exe
])
