# 2021-2022

## Limitations

Directories `pelican-themes/` and `pelican-plugins/` are ignored via this repo's `.gitignore` file. Nevertheless, they are expected to contain build dependencies. In order to set up your build environment, please run the following commands in the top directory of your repo:
```sh
$ git clone https://github.com/getpelican/pelican-themes
$ git clone https://github.com/getpelican/pelican-plugins
```
These two repositories used to be included as submodules. But disappearing submodules (repo deleted by user)  within these repositories, hundered the website's deployment at gh-pages.
