#!/usr/bin/env python
#
# Windows Azure Linux Agent
#
# Copyright 2014 Microsoft Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Requires Python 2.4+ and Openssl 1.0+
#

LibDir = '/var/lib/waagent'
ConfFilePath = '/etc/waagent.conf' 
LogFilePath = '/var/log/waagent.log'
ConsoleFilePath = '/dev/console'

def SetFileContent(path, content):
    pass

def GetFileContet(path):
    pass

def RestartNetwork():
    pass

def OpenPortForDhcp():
    #Open DHCP port if iptables is enabled.
    Run("iptables -D INPUT -p udp --dport 68 -j ACCEPT",chk_err=False)  # We supress error logging on error.
    Run("iptables -I INPUT -p udp --dport 68 -j ACCEPT",chk_err=False)  # We supress error logging on error.