{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'face_recognition'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-aa2632447a5e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mcv2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mface_recognition\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mPIL\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mImage\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mImageDraw\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'face_recognition'"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import face_recognition\n",
    "from PIL import Image,ImageDraw"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting dlib\n",
      "  Using cached dlib-19.21.1.tar.gz (3.6 MB)\n",
      "Building wheels for collected packages: dlib\n",
      "  Building wheel for dlib (setup.py): started\n",
      "  Building wheel for dlib (setup.py): finished with status 'error'\n",
      "  Running setup.py clean for dlib\n",
      "Failed to build dlib\n",
      "Installing collected packages: dlib\n",
      "    Running setup.py install for dlib: started\n",
      "    Running setup.py install for dlib: finished with status 'error'\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  ERROR: Command errored out with exit status 1:\n",
      "   command: 'C:\\Users\\harib\\anaconda3\\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '\"'\"'C:\\\\Users\\\\harib\\\\AppData\\\\Local\\\\Temp\\\\pip-install-0hfsz9yl\\\\dlib\\\\setup.py'\"'\"'; __file__='\"'\"'C:\\\\Users\\\\harib\\\\AppData\\\\Local\\\\Temp\\\\pip-install-0hfsz9yl\\\\dlib\\\\setup.py'\"'\"';f=getattr(tokenize, '\"'\"'open'\"'\"', open)(__file__);code=f.read().replace('\"'\"'\\r\\n'\"'\"', '\"'\"'\\n'\"'\"');f.close();exec(compile(code, __file__, '\"'\"'exec'\"'\"'))' bdist_wheel -d 'C:\\Users\\harib\\AppData\\Local\\Temp\\pip-wheel-rl68iqc7'\n",
      "       cwd: C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\\n",
      "  Complete output (58 lines):\n",
      "  running bdist_wheel\n",
      "  running build\n",
      "  running build_py\n",
      "  package init file 'tools\\python\\dlib\\__init__.py' not found (or not a regular file)\n",
      "  running build_ext\n",
      "  Building extension for Python 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)]\n",
      "  Invoking CMake setup: 'cmake C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\tools\\python -DCMAKE_LIBRARY_OUTPUT_DIRECTORY=C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\build\\lib.win-amd64-3.8 -DPYTHON_EXECUTABLE=C:\\Users\\harib\\anaconda3\\python.exe -DCMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE=C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\build\\lib.win-amd64-3.8 -A x64'\n",
      "  -- Building for: NMake Makefiles\n",
      "  CMake Error at CMakeLists.txt:5 (message):\n",
      "  \n",
      "  \n",
      "  \n",
      "    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n",
      "  \n",
      "  \n",
      "    You must use Visual Studio to build a python extension on windows.  If you\n",
      "    are getting this error it means you have not installed Visual C++.  Note\n",
      "    that there are many flavors of Visual Studio, like Visual Studio for C#\n",
      "    development.  You need to install Visual Studio for C++.\n",
      "  \n",
      "  \n",
      "    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n",
      "  \n",
      "  \n",
      "  \n",
      "  \n",
      "  -- Configuring incomplete, errors occurred!\n",
      "  Traceback (most recent call last):\n",
      "    File \"<string>\", line 1, in <module>\n",
      "    File \"C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\setup.py\", line 223, in <module>\n",
      "      setup(\n",
      "    File \"C:\\Users\\harib\\anaconda3\\lib\\site-packages\\setuptools\\__init__.py\", line 153, in setup\n",
      "      return distutils.core.setup(**attrs)\n",
      "    File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\core.py\", line 148, in setup\n",
      "      dist.run_commands()\n",
      "    File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\dist.py\", line 966, in run_commands\n",
      "      self.run_command(cmd)\n",
      "    File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\dist.py\", line 985, in run_command\n",
      "      cmd_obj.run()\n",
      "    File \"C:\\Users\\harib\\anaconda3\\lib\\site-packages\\wheel\\bdist_wheel.py\", line 290, in run\n",
      "      self.run_command('build')\n",
      "    File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\cmd.py\", line 313, in run_command\n",
      "      self.distribution.run_command(command)\n",
      "    File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\dist.py\", line 985, in run_command\n",
      "      cmd_obj.run()\n",
      "    File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\command\\build.py\", line 135, in run\n",
      "      self.run_command(cmd_name)\n",
      "    File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\cmd.py\", line 313, in run_command\n",
      "      self.distribution.run_command(command)\n",
      "    File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\dist.py\", line 985, in run_command\n",
      "      cmd_obj.run()\n",
      "    File \"C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\setup.py\", line 135, in run\n",
      "      self.build_extension(ext)\n",
      "    File \"C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\setup.py\", line 172, in build_extension\n",
      "      subprocess.check_call(cmake_setup, cwd=build_folder)\n",
      "    File \"C:\\Users\\harib\\anaconda3\\lib\\subprocess.py\", line 364, in check_call\n",
      "      raise CalledProcessError(retcode, cmd)\n",
      "  subprocess.CalledProcessError: Command '['cmake', 'C:\\\\Users\\\\harib\\\\AppData\\\\Local\\\\Temp\\\\pip-install-0hfsz9yl\\\\dlib\\\\tools\\\\python', '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=C:\\\\Users\\\\harib\\\\AppData\\\\Local\\\\Temp\\\\pip-install-0hfsz9yl\\\\dlib\\\\build\\\\lib.win-amd64-3.8', '-DPYTHON_EXECUTABLE=C:\\\\Users\\\\harib\\\\anaconda3\\\\python.exe', '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE=C:\\\\Users\\\\harib\\\\AppData\\\\Local\\\\Temp\\\\pip-install-0hfsz9yl\\\\dlib\\\\build\\\\lib.win-amd64-3.8', '-A', 'x64']' returned non-zero exit status 1.\n",
      "  ----------------------------------------\n",
      "  ERROR: Failed building wheel for dlib\n",
      "    ERROR: Command errored out with exit status 1:\n",
      "     command: 'C:\\Users\\harib\\anaconda3\\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '\"'\"'C:\\\\Users\\\\harib\\\\AppData\\\\Local\\\\Temp\\\\pip-install-0hfsz9yl\\\\dlib\\\\setup.py'\"'\"'; __file__='\"'\"'C:\\\\Users\\\\harib\\\\AppData\\\\Local\\\\Temp\\\\pip-install-0hfsz9yl\\\\dlib\\\\setup.py'\"'\"';f=getattr(tokenize, '\"'\"'open'\"'\"', open)(__file__);code=f.read().replace('\"'\"'\\r\\n'\"'\"', '\"'\"'\\n'\"'\"');f.close();exec(compile(code, __file__, '\"'\"'exec'\"'\"'))' install --record 'C:\\Users\\harib\\AppData\\Local\\Temp\\pip-record-yhmi10s8\\install-record.txt' --single-version-externally-managed --compile --install-headers 'C:\\Users\\harib\\anaconda3\\Include\\dlib'\n",
      "         cwd: C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\\n",
      "    Complete output (60 lines):\n",
      "    running install\n",
      "    running build\n",
      "    running build_py\n",
      "    package init file 'tools\\python\\dlib\\__init__.py' not found (or not a regular file)\n",
      "    running build_ext\n",
      "    Building extension for Python 3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)]\n",
      "    Invoking CMake setup: 'cmake C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\tools\\python -DCMAKE_LIBRARY_OUTPUT_DIRECTORY=C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\build\\lib.win-amd64-3.8 -DPYTHON_EXECUTABLE=C:\\Users\\harib\\anaconda3\\python.exe -DCMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE=C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\build\\lib.win-amd64-3.8 -A x64'\n",
      "    -- Building for: NMake Makefiles\n",
      "    CMake Error at CMakeLists.txt:5 (message):\n",
      "    \n",
      "    \n",
      "    \n",
      "      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n",
      "    \n",
      "    \n",
      "      You must use Visual Studio to build a python extension on windows.  If you\n",
      "      are getting this error it means you have not installed Visual C++.  Note\n",
      "      that there are many flavors of Visual Studio, like Visual Studio for C#\n",
      "      development.  You need to install Visual Studio for C++.\n",
      "    \n",
      "    \n",
      "      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n",
      "    \n",
      "    \n",
      "    \n",
      "    \n",
      "    -- Configuring incomplete, errors occurred!\n",
      "    Traceback (most recent call last):\n",
      "      File \"<string>\", line 1, in <module>\n",
      "      File \"C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\setup.py\", line 223, in <module>\n",
      "        setup(\n",
      "      File \"C:\\Users\\harib\\anaconda3\\lib\\site-packages\\setuptools\\__init__.py\", line 153, in setup\n",
      "        return distutils.core.setup(**attrs)\n",
      "      File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\core.py\", line 148, in setup\n",
      "        dist.run_commands()\n",
      "      File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\dist.py\", line 966, in run_commands\n",
      "        self.run_command(cmd)\n",
      "      File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\dist.py\", line 985, in run_command\n",
      "        cmd_obj.run()\n",
      "      File \"C:\\Users\\harib\\anaconda3\\lib\\site-packages\\setuptools\\command\\install.py\", line 61, in run\n",
      "        return orig.install.run(self)\n",
      "      File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\command\\install.py\", line 545, in run\n",
      "        self.run_command('build')\n",
      "      File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\cmd.py\", line 313, in run_command\n",
      "        self.distribution.run_command(command)\n",
      "      File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\dist.py\", line 985, in run_command\n",
      "        cmd_obj.run()\n",
      "      File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\command\\build.py\", line 135, in run\n",
      "        self.run_command(cmd_name)\n",
      "      File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\cmd.py\", line 313, in run_command\n",
      "        self.distribution.run_command(command)\n",
      "      File \"C:\\Users\\harib\\anaconda3\\lib\\distutils\\dist.py\", line 985, in run_command\n",
      "        cmd_obj.run()\n",
      "      File \"C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\setup.py\", line 135, in run\n",
      "        self.build_extension(ext)\n",
      "      File \"C:\\Users\\harib\\AppData\\Local\\Temp\\pip-install-0hfsz9yl\\dlib\\setup.py\", line 172, in build_extension\n",
      "        subprocess.check_call(cmake_setup, cwd=build_folder)\n",
      "      File \"C:\\Users\\harib\\anaconda3\\lib\\subprocess.py\", line 364, in check_call\n",
      "        raise CalledProcessError(retcode, cmd)\n",
      "    subprocess.CalledProcessError: Command '['cmake', 'C:\\\\Users\\\\harib\\\\AppData\\\\Local\\\\Temp\\\\pip-install-0hfsz9yl\\\\dlib\\\\tools\\\\python', '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=C:\\\\Users\\\\harib\\\\AppData\\\\Local\\\\Temp\\\\pip-install-0hfsz9yl\\\\dlib\\\\build\\\\lib.win-amd64-3.8', '-DPYTHON_EXECUTABLE=C:\\\\Users\\\\harib\\\\anaconda3\\\\python.exe', '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE=C:\\\\Users\\\\harib\\\\AppData\\\\Local\\\\Temp\\\\pip-install-0hfsz9yl\\\\dlib\\\\build\\\\lib.win-amd64-3.8', '-A', 'x64']' returned non-zero exit status 1.\n",
      "    ----------------------------------------\n",
      "ERROR: Command errored out with exit status 1: 'C:\\Users\\harib\\anaconda3\\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '\"'\"'C:\\\\Users\\\\harib\\\\AppData\\\\Local\\\\Temp\\\\pip-install-0hfsz9yl\\\\dlib\\\\setup.py'\"'\"'; __file__='\"'\"'C:\\\\Users\\\\harib\\\\AppData\\\\Local\\\\Temp\\\\pip-install-0hfsz9yl\\\\dlib\\\\setup.py'\"'\"';f=getattr(tokenize, '\"'\"'open'\"'\"', open)(__file__);code=f.read().replace('\"'\"'\\r\\n'\"'\"', '\"'\"'\\n'\"'\"');f.close();exec(compile(code, __file__, '\"'\"'exec'\"'\"'))' install --record 'C:\\Users\\harib\\AppData\\Local\\Temp\\pip-record-yhmi10s8\\install-record.txt' --single-version-externally-managed --compile --install-headers 'C:\\Users\\harib\\anaconda3\\Include\\dlib' Check the logs for full command output.\n"
     ]
    }
   ],
   "source": [
    "pip install dlib\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting cmake\n",
      "  Downloading cmake-3.18.4.post1-py3-none-win_amd64.whl (34.7 MB)\n",
      "Installing collected packages: cmake\n",
      "Successfully installed cmake-3.18.4.post1\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install cmake"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
