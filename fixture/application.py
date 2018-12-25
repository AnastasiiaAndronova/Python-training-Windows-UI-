# -*- coding: utf-8 -*-
import clr
import sys
import os.path
import sys

project_dir=os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir+ "\\..\\lib\\")

clr.AddReferenceByName("TestStack.White")
from TestStack.White import  Application
from TestStack.White.InputDevices  import  Keyboard
from TestStack.White.WindowsAPI   import  KeyboardInput

from TestStack.White.UIItems.Finders import *


clr.AddReferenceByName("UiAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35")

from System.Windows.Automation import *


class WinApp:

    def __init__(self,appname):
        self.application=Application.Launch(appname)
        self.main_window=self.application.GetWindow("Free Address Book")

    def destroy(self):
        self.main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()

    def close_group_editor(self):
        self.modal.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()

    def add_new_group(self,groupname):
        self.open_group_editor()
        self.modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
        self.modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter(groupname)
        Keyboard.Instance.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN)
        self.close_group_editor()

    def delete_group(self,line):
        self.open_group_editor()
        tree = self.group_list = self.modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
        root = tree.Nodes[0]
        root.Nodes[line].Click()
        self.modal.Get(SearchCriteria.ByAutomationId("uxDeleteAddressButton")).Click()
        newmodal=self.main_window.ModalWindow("Group editor")
        newmodal.Get(SearchCriteria.ByAutomationId("uxOKAddressButton")).Click()

        self.close_group_editor()


    def open_group_editor(self):
        self.main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
        self.modal=self.main_window.ModalWindow("Group editor")


    def get_group_list(self):
        self.open_group_editor()
        tree=self.group_list=self.modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
        root=tree.Nodes[0]
        l=[node.Text for node in root.Nodes ]

        self.close_group_editor()
        return l


