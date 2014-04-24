# -*- Mode: python; coding: utf-8; tab-width: 4; indent-tabs-mode: nil; -*-
#
# Copyright (C) 2012 - fossfreedom
# Copyright (C) 2012 - Agustin Carrasco
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of thie GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301  USA.

from gi.repository import GObject, Peas, Gtk

class CloseOnHide(GObject.Object, Peas.Activatable):
    object = GObject.property(type=GObject.GObject)

    def __init__(self):
        super(CloseOnHide, self).__init__()

    def do_activate(self):
        self.window = self.object.get_property("window")
        self.handler_id = self.window.connect("hide", self.hide_event_cb)
        self.shell = self.object

    def do_deactivate(self):
        self.window.show()
        self.window.disconnect(self.handler_id) 

    def hide_event_cb(self, widget):
        player = self.shell.props.shell_player
        if player.get_playing():
            player.stop()
            self.window.emit('delete-event', None) 
            
            return False
            
        return True
