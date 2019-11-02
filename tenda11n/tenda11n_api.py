import requests

# Tenda11N Unofficial API
# Ver: 1.0 (2019/11/02)
# Credits: deniz.frosty@gmail.com | deniz617@github
# Tested on Tenda11N Router, Sys Ver: V5.07.46_en

class Tenda11N:
    def __init__(self, routerIP="192.168.0.1"):
        self.routerIP = routerIP
        self.session = requests.Session()

    def __extract_CtrlList_fromHTML(self, htmlStr):
        strPos1 = htmlStr.find("new Array(")
        if (strPos1 != -1):
            strPos2 = htmlStr.find(");", strPos1)
            if(strPos2 != -1):
                newstr = (htmlStr[strPos1 + 11:strPos2 - 1])
                str_tokens = newstr.split("','")
                return str_tokens
        return False

    def login(self, user, pw):
        session = self.session

        url = "http://" + self.routerIP + "/LoginCheck"

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "http://" + self.routerIP,
            "Referer": "http://" + self.routerIP + "/login.asp"
        }

        postdata = {"Username": user, "checkEn": "0", "Password": pw}

        try:
            res = session.post(url, headers=headers, data=postdata, verify=False, timeout=15)

            if res:
                if (res.text.find("Wrong password") == -1):
                    return True
        except:
            return False

        return False

    def networkUsageStats(self):
        session = self.session

        url = "http://" + self.routerIP + "/goform/updateIptAccount"

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "text/plain;charset=UTF-8",
            "Origin": "http://" + self.routerIP,
            "Referer": "http://" + self.routerIP + "/sys_iptAccount.asp"
        }

        postdata = {"something"}

        ip_table = {}

        try:
            res = session.post(url, headers, postdata, verify=False, timeout=5)

            ip_tokens = res.text.split("\n")

            for ip in ip_tokens:
                arg_split = ip.split(";")
                if (len(arg_split) > 1):
                    ip_table[arg_split[0]] = {
                        "Uplink": arg_split[1], "Downlink": arg_split[2], "TUpMB": arg_split[4], "TDownMB": arg_split[6]
                    }
        finally:
            return ip_table

    def getBandwithCtrl_List(self):
        session = self.session

        url = "http://" + self.routerIP + "/net_tc.asp"

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "http://" + self.routerIP + "/advance.asp"
        }

        try:
            res = session.get(url, headers=headers, verify=False, timeout=5)
            if res:
                return self.__extract_CtrlList_fromHTML(res.text)
        except:
            return False

        return False

    def setBandwithCtrl_List(self, bandwithCtrl_flag, ctrl_list):
        session = self.session

        url = "http://" + self.routerIP + "/goform/trafficForm?GO=net_tc.asp&tc_enable=" + \
            str(bandwithCtrl_flag)

        url += "&up_Band=12800&down_Band=12800&cur_number="

        url += str(len(ctrl_list))

        for index, rule in enumerate(ctrl_list, start=1):
            url += "&tc_list_" + str(index)
            url += "=" + rule

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "http://" + self.routerIP + "/net_tc.asp"
        }

        try:
            res = session.get(url, headers=headers, verify=False, timeout=5)
            if res:
                return self.__extract_CtrlList_fromHTML(res.text)
        except:
            return False

        return False

    def reboot(self):
        session = self.session

        url = "http://" + self.routerIP + "/goform/SysToolReboot"

        headers = {
            "User-Agent": "Mozilla/5.0",
            "If-Modified-Since": "0",
            "Referer": "http://" + self.routerIP + "/system_reboot.asp"
        }

        try:
            session.get(url, headers=headers, verify=False, timeout=1)
        finally:
            return
