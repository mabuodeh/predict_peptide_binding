import pathlib
from setuptools import setup

README = (pathlib.Path(__file__).parent / "README.md").read_text()

setup(
    name="predict_peptide_binding",
    version="1.0.0",
    long_description=README,
    long_description_content_type="text/markdown",
    package=["predict_peptide_binding"],
    install_requires=["pandas", "requests", "xlsxwriter"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "predict=predict_peptide_binding.__main__:main",
        ]
    }
)