#!/usr/bin/python3

# 2020
# Bộ công cụ Raven-Storm được lập trình và phát triển bởi Taguar258.
# Bộ công cụ Raven-Storm được xuất bản theo Giấy phép MIT.
# Bộ công cụ Raven-Storm dựa trên CLIF-Framework.
# CLIF-Framework được lập trình và phát triển bởi Taguar258.
# CLIF-Framework được xuất bản theo Giấy phép MIT.

from sys import argv

from CLIF_Framework.framework import console, module  # noqa: I900


def run():
	main_console = console()
	main_console.rsversion = "4.1 (Pre)"
	main_console.user_argv = argv

	module("modules.main", main_console)

	main_console.run()


if __name__ == "__main__":
	run()
