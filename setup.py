
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="the-money-converter",
    version="1.0.1",
    author="GetDream_1996",
    author_email="543046534@qq.com",
    description="货币汇率转换",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KILLER2017/the-money-converter",
    #project_urls={},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.0",
    install_requires=['requests', 'bs4', 'lxml']
)