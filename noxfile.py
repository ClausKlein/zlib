import nox

# It's a good idea to keep your dev session out of the default list
# so it's not run twice accidentally
# @nox.session(default=False)
# def dev(session: nox.Session) -> None:
#     """
#     Set up a python development environment for the project at ".venv".
#     """
#     session.install("virtualenv")
#     session.run("virtualenv", ".venv", silent=True)
#     # Use the venv's interpreter to install the project along with
#     # all it's dev dependencies, this ensures it's installed in the right way
#     session.run(".venv/bin/pip", "install", "-f", "requierments.txt", external=True)


@nox.session
def build(session: nox.Session) -> None:
    prefix = "C:/ZLIB/1.2.5/win32-msvc-14.0"
    session.install("cmake")
    session.install("ninja")
    session.run(
        "cmake",
        "-B",
        "build",
        "-S",
        ".",
        "-G",
        "Ninja",
        "-D",
        "CMAKE_C_COMPILER=cl",
        "-D",
        "CMAKE_BUILD_TYPE=Release",
        "-D",
        f"CMAKE_INSTALL_PREFIX={prefix}",
        "--fresh",
    )
    # session.run("cmake", "--build", "build", "--config", "Release")
    session.run("cmake", "--build", "build", "--config", "Release", "--target", "test")
    session.run(
        "cmake", "--build", "build", "--config", "Release", "--target", "package"
    )
    session.run(
        "cmake", "--install", "build", "--config", "Release", "--prefix", prefix
    )


# @nox.session
# def test(session: nox.Session) -> None:
#     session.install("gcovr")
#     session.run("cmake", "--build", "build", "--config", "Release", "--target", "test")
#     session.run("gcovr", "--root", "build")
