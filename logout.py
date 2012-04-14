'''u413 - an open-source BBS/terminal/PI-themed forum
	Copyright (C) 2012 PiMaster
	Copyright (C) 2012 EnKrypt

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU Affero General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU Affero General Public License for more details.

	You should have received a copy of the GNU Affero General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.'''

import command
import database as db

<<<<<<< HEAD
def logout_func(args,u413):
	if u413.user.username!="Guest":
		u413.type(u413.user.logout())
=======
def logout_func(args,user):
	out=command.Command.json.copy()
	if user.username!="Guest":
		out.update({
			"DisplayItems":[display.Item(user.logout())]
		})
>>>>>>> 31dd46dea58cff98b0e37e86850d4080466161e3
	else:
		u413.type("You are not logged in")
	return out

command.Command("LOGOUT","Logs out a user who is logged into U413",logout_func,10)
