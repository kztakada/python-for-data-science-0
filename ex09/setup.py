from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from setuptools import setup
from wheel.bdist_wheel import bdist_wheel


class BdistWheel(bdist_wheel):
    def run(self):
        super().run()

        for wheel_path in Path(self.dist_dir).glob("*.whl"):
            with NamedTemporaryFile(
                dir=wheel_path.parent,
                delete=False,
                suffix=".whl",
            ) as temporary:
                temporary_path = Path(temporary.name)

            with ZipFile(wheel_path, "r") as source:
                with ZipFile(temporary_path, "w", ZIP_DEFLATED) as destination:
                    for item in source.infolist():
                        if item.filename.endswith("/setup.py"):
                            continue
                        data = source.read(item.filename)
                        if item.filename.endswith(".dist-info/METADATA"):
                            data = data.replace(
                                b"Name: ft-package",
                                b"Name: ft_package",
                            )
                        destination.writestr(item, data)

            temporary_path.replace(wheel_path)


setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/katakada/ft_package",
    author="katakada",
    author_email="katakada@student.42tokyo.jp",
    license="MIT",
    python_requires=">=3.10",
    packages=["ft_package"],
    package_dir={"ft_package": "."},
    cmdclass={"bdist_wheel": BdistWheel},
)
