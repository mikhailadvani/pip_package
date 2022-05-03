import setuptools

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()
    install_requires = []
    for dependency in requirements:
      if dependency.startswith("git+"):
        package_name = dependency.split("/")[-1].split("@")[0]
        dependency = package_name + ' @ ' + dependency
        print(dependency)
      install_requires.append(dependency)

setuptools.setup(
    name="pip_package",
    version="0.0.1",
    author="Mikhail Advani",
    url="https://github.com/mikhailadvani/pip_package",
    install_requires=install_requires
)
