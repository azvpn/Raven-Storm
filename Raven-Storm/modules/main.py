# 2020
# Bộ công cụ Raven-Storm được lập trình và phát triển bởi Taguar258.
# Bộ công cụ Raven-Storm được xuất bản theo Giấy phép MIT.
# Bộ công cụ Raven-Storm dựa trên CLIF-Framework.
# CLIF-Framework được lập trình và phát triển bởi Taguar258.
# CLIF-Framework được xuất bản theo Giấy phép MIT.

from os import chdir, path, system
from random import choice
from time import sleep

import requests
from CLIF_Framework.framework import console  # noqa: I900
from CLIF_Framework.framework import event  # noqa: I900
from CLIF_Framework.framework import module  # noqa: I900
from CLIF_Framework.framework import tools  # noqa: I900

try:
	import readline  # noqa: F401
except Exception:  # noqa: S110
	pass


event = event()
tools = tools()


class Main:
	def __init__(selfie, console):  # noqa: N805
		global var
		global self
		self = selfie
		var = console  # noqa: VNE002

		var.modules = {}
		self._add_commands()

		# Colors
		var.C_None = "\x1b[0;39m"
		var.C_Bold = "\x1b[1;39m"
		var.C_Green = "\x1b[32m"
		var.C_Violet = "\x1b[0;35m"
		var.C_Dark_Blue = "\x1b[34m"
		var.C_Red = "\x1b[31m"
		var.C_Yellow = "\x1b[33m"
		var.C_Cyan = "\x1b[36m"

		# var.C_Blink = "\x1b[5;39m"
		# #var.C_Magenta = "\x1b[35m"
		# var.C_BRed = "\x1b[1;31m"
		# var.C_BGreen = "\x1b[1;32m"
		# var.C_BYellow = "\x1b[1;33m"
		# var.C_BBlue = "\x1b[1;34m"
		# #var.C_BCyan = "\x1b[1;36m"
		var.C_Magenta = "\x1b[1;35m"

		var.session = [[False, ""], [False, []]]  # [Save, path], [Load, Commands_to_run]
		var.server = [False, True, "ip", "pass", 1]  # Enabled, HOST/CLIENT, URL, PASSWORD, COMMAND_NUMBER
		if len(var.user_argv) != 1:
			if var.user_argv[1] == "--connect":
				var.server = [True, False, var.user_argv[2], var.user_argv[3], 1]
				status = requests.post((var.server[2] + "reset"), data={"password": var.server[3]}).text

	# def generate_quote(self):
	# 	quote = choice(["Quote",
	# 					"Other Examples."])

	# 	len_of_line = (int(59 / 2) - int(len(quote) / 2))
	# 	splitter = "|"

	# 	text = (((len_of_line - 1) * " ") + splitter + quote + splitter)
	# 	text_len = len(text)
	# 	box_border = (((len_of_line - 1) * " ") + ("-" * (text_len - len_of_line + 1)))

	# 	return text + "\n" + box_border

	def banner(self):  # """ + self.generate_quote() + """
		# banner_fire_color = var.C_Cyan
		# banner_middle_color = var.C_Violet
		# banner_bottom_color = var.C_Dark_Blue
		banner_fire_color = var.C_Cyan
		banner_middle_color = var.C_Violet
		banner_bottom_color = var.C_Dark_Blue
		banner_logo = ("""C_Bo-----------------------------------------------------------C_W
C_FIRE (
 )\\ )                                 )                C_WC_Bov.""" + var.rsversion + """C_WC_FIRE
(()/(    )   )      (              ( /(      (       )
 /(_))( /(  /((    ))\\  (      (   )\\()) (   )(     (
(C_MID_C_FIRE))  )(_))(_))\\  /((_) )\\ )   )\\ (C_MID_C_FIRE))/  )\\ (()\\    )\\  'C_MID
| _ \\C_FIRE((C_MID_C_FIRE)C_MID_ _C_FIRE)((C_MID_C_FIRE)(C_MID_C_FIRE))  C_MID_C_FIRE(C_MID_C_FIRE/(  ((C_MID_C_FIRE)C_MID| |C_FIRE  ((C_MID_C_FIRE) ((C_MID_C_FIRE) C_MID_C_FIRE((C_MID_C_FIRE))C_MID
|   // _` |\\ V / / -_)| ' \\)) (_-<|  _|/ _ \\| '_|| '  \\C_FIRE()C_BOT
|_|_\\\\__,_| \\_/  \\___||_||_|  /__/ \\__|\\___/|_|  |_|_|_|C_W

C_BoS Stress-Testing-Toolkit của Taguar258 (c) | MIT 2020
Dịch bởi Đậu Đậu | Dựa trên Khung CLIF của Taguar258 (c) | MIT 2020C_W

BẰNG CÁCH SỬ DỤNG PHẦN MỀM NÀY, BẠN PHẢI ĐỒNG Ý CHỊU TRÁCH NHIỆM ĐẦY ĐỦ
ĐỐI VỚI BẤT KỲ THIỆT HẠI NÀO DO RAVEN-STORM gây ra.
RAVEN-STORM KHÔNG NÊN ĐỀ XUẤT NHỮNG NGƯỜI THỰC HIỆN CÁC HOẠT ĐỘNG BẤT HỢP PHÁP.
C_Bo-----------------------------------------------------------C_W""")
		banner_logo = banner_logo.replace("C_W", var.C_None)
		banner_logo = banner_logo.replace("C_Bo", var.C_Bold)
		banner_logo = banner_logo.replace("C_FIRE", banner_fire_color)
		banner_logo = banner_logo.replace("C_MID", banner_middle_color)
		banner_logo = banner_logo.replace("C_BOT", banner_bottom_color)
		print(banner_logo)

	@event.event
	def on_ready():
		system("clear || cls")
		self.banner()
		self.help()

	@event.event
	def on_command_not_found(command):
		print("")
		print("Lệnh bạn đã nhập không tồn tại.")
		print("")

	def exit_console(self):
		print("Chúc một ngày tốt lành.")
		quit()

	@event.event
	def on_command(command):
		if var.session[0][0]:
			var.session[0][1].write(command + "\n")
		if var.server[0] and var.server[1]:
			status = requests.post((var.server[2] + "set/com"), data={"password": var.server[3], "data": command}).text
			if status != "200":
				print("")
				print("Đã xảy ra lỗi khi gửi lệnh tới máy chủ.")
				print("")

	def _add_commands(self):
		event.commands(self.exit_console, ["exit", "quit", "e", "q"])
		event.commands(self.run_shell, ".")
		event.commands(self.debug, "$")
		event.commands(self.help, "help")
		event.parser(self.run_debug_arg, "$")
		event.parser(self.run_shell_arg, ".")
		event.help(["exit", "quit", "e", "q"], "Thoát Raven-Storm.")
		event.help("help", "Xem tất cả các lệnh.")
		event.help("upgrade", "Nâng cấp Raven-Storm.")
		event.help(".", "Chạy lệnh shell.")
		event.help("clear", "Xóa màn hình.")
		event.help("record", "Lưu phiên này.")
		event.help("load", "Làm lại một phiên bằng cách sử dụng tệp phiên.")
		event.help("ddos", "Ckết nối với máy chủ Raven-Storm.")
		event.help_comment("\nModules:")
		event.help("l4", "Tải mô-đun layer4. (UDP/TCP)")
		event.help("l3", "Tải mô-đun layer3. (ICMP)")
		event.help("l7", "Tải mô-đun layer7. (HTTP)")
		event.help("bl", "Tải mô-đun bluetooth. (L2CAP)")
		event.help("arp", "Tải mô-đun giả mạo arp. (ARP)")
		event.help("wifi", "Tải mô-đun wifi. (IEEE)")
		event.help("server", "Tải mô-đun máy chủ cho các cuộc tấn công DDos.")
		event.help("scanner", "Tải mô-đun máy quét.")

		var.modules["Layer4"] = console()
		var.modules["Layer3"] = console()
		var.modules["Layer7"] = console()
		var.modules["BL"] = console()
		var.modules["ARP"] = console()
		var.modules["Scanner"] = console()
		var.modules["Server"] = console()
		var.modules["WIFI"] = console()

	def run_shell(self, command):
		system(command)

	def check_session(self):
		if var.session[1][0] and len(var.session[1][1]) >= 1:
			if len(var.session[1][1][0]) >= 1:
				run_following = [var.session[1][1][0][0], var.session[1][1][0][0]]
				var.session[1][1][0] = var.session[1][1][0][1:]
			else:
				var.session[1][1] = var.session[1][1][1:]
				run_following = [var.session[1][1][0][0], var.session[1][1][0][0]]
				var.session[1][1][0] = var.session[1][1][0][1:]
			var.run_command = run_following

	@event.event
	def on_input():
		self.check_session()
		if var.server[0] and not var.server[1]:
			while True:
				data = requests.post((var.server[2] + ("get/com%s" % var.server[4])), data={"password": var.server[3]}).text
				if data != "500":
					var.server[4] = var.server[4] + 1
					var.run_command = [data, data]
					print(var.ps1 + "\r")
					break
				else:
					sleep(1)

	def run_shell_arg(self, command):
		return tools.arg("Nhập lệnh shell: ", ". ", command)
		print("", end="")

	def debug(self, command):
		eval(command)

	def run_debug_arg(self, command):
		return tools.arg("Nhập lệnh gỡ lỗi: ", "$ ", command)
		print("", end="")

	@event.command
	def l4():
		module("modules.l4.main", var.modules["Layer4"])
		var.modules["Layer4"].session = var.session
		var.modules["Layer4"].server = var.server
		var.modules["Layer4"].run()

	@event.command
	def l3():
		module("modules.l3.main", var.modules["Layer3"])
		var.modules["Layer3"].session = var.session
		var.modules["Layer3"].server = var.server
		var.modules["Layer3"].run()

	@event.command
	def l7():
		module("modules.l7.main", var.modules["Layer7"])
		var.modules["Layer7"].session = var.session
		var.modules["Layer7"].server = var.server
		var.modules["Layer7"].run()

	@event.command
	def bl():
		module("modules.bl.main", var.modules["BL"])
		var.modules["BL"].session = var.session
		var.modules["BL"].server = var.server
		var.modules["BL"].run()

	@event.command
	def arp():
		module("modules.arp.main", var.modules["ARP"])
		var.modules["ARP"].session = var.session
		var.modules["ARP"].server = var.server
		var.modules["ARP"].run()

	@event.command
	def wifi():
		module("modules.wifi.main", var.modules["WIFI"])
		var.modules["WIFI"].session = var.session
		var.modules["WIFI"].server = var.server
		var.modules["WIFI"].run()

	@event.command
	def scanner():
		module("modules.scanner.main", var.modules["Scanner"])
		var.modules["Scanner"].session = var.session
		var.modules["Scanner"].server = var.server
		var.modules["Scanner"].run()

	@event.command
	def server():
		module("modules.server.main", var.modules["Server"])
		var.modules["Server"].session = var.session
		var.modules["Server"].server = var.server
		var.modules["Server"].run()

	def help(self):
		event.help_title("\x1b[1;39mHelp:\x1b[0;39m")
		tools.help("|-- ", " :: ", event)
		print("")

	@event.command
	def ddos(self):
		print("")
		try:
			ddos_host = input("Nhập URL máy chủ của máy chủ: ")
			ddos_password = input("Nhập mật khẩu: ")
			if "http" not in ddos_host:
				raise Exception("URL máy chủ lưu trữ sai.")
			if "/" != ddos_host[-1]:
				ddos_host += "/"
			test_data = {"password": ddos_password}
			agreed = requests.post((ddos_host + "get/agreed"), data=test_data).text
			if agreed != "False":
				raise Exception("Dữ liệu sai đã được cung cấp.")
			ddos_role = tools.question("Bạn có muốn cái này được sử dụng như một máy chủ lưu trữ?")
			status = requests.post((ddos_host + "reset"), data=test_data).text
			if status != "200":
				print("Một vài chuyện lạ đã xảy ra.")
			var.server[1] = ddos_role
			var.server[2] = ddos_host
			var.server[3] = ddos_password
			var.server[0] = True
		except Exception as ex:
			print("Một ngoại lệ đã xảy ra.", ex)
		print("")

	@event.command
	def record(command):
		print("")
		try:
			to_file = tools.arg("Lưu vào tệp: ", "record ", command)
			if path.isfile(to_file):
				raise Exception("Tập tin đã tồn tại.")
			else:
				new_file = open(to_file, "w")
				# new_file.write("# -- Session File")
				new_file.close()
				var.session[0][1] = open(to_file, "a")
				var.session[0][0] = True
				print("")
				print("Ghi âm...")
		except Exception as ex:
			print("Đã xảy ra lỗi.", ex)
		print("")

	@event.command
	def load(command):
		print("")
		try:
			from_file = tools.arg("Tải từ tệp: ", "load ", command)
			if not path.isfile(from_file):
				raise Exception("Tập tin không tồn tại.")
			else:
				new_list = []
				command_list = []
				for item in open(from_file, "r").read().split("\n"):
					if item != "":
						new_list.append(item)
						if item in ["e", "q", "exit", "quit"]:
							command_list.append(new_list)
							new_list = []
						elif item in ["l4", "l3", "l7", "ble", "arp", "scanner", "server"]:
							command_list.append(new_list)
							new_list = []
						else:
							pass
				command_list.append(new_list)
				var.session[1][1] = command_list
				var.session[1][0] = True
				print("Hành động lặp lại...")
		except Exception as ex:
			print("Đã xảy ra lỗi.", ex)
		print("")

	@event.command
	def upgrade():
		try:
			chdir("/tmp")
			system("sudo git clone https://github.com/DauDau432/Raven-Storm.git")
			chdir("/tmp/Raven-Storm/")
			system("sudo bash ./install_to_bin.sh")
			print("[i] Xóa Raven-Storm được lưu trữ tạm thời...")
			system("sudo rm -rf -i /tmp/Raven-Storm/")
			var.stop()
			quit()
		except Exception:
			print("Không thể nâng cấp Raven-Storm. (Đảm bảo sử dụng sudo)")

	@event.command
	def clear():
		system("clear || cls")

	@event.event
	def on_command():
		print("", end="")

	@event.event
	def on_interrupt():
		self.exit_console()


def setup(console):
	console.ps1 = ">> "
	console.add(Main(console), event)
