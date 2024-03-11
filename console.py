#!/usr/bin/env python3
"""This module houses the HBNB class definition
and its attributes and methods"""

import cmd
import sys
import os

sys.path.append(os.getcwd())
try:
    from models.base_model import BaseModel
    from models import storage
except Exception as e:
    print(e)


class HBNBCommand(cmd.Cmd):
    """This class houses the configuration of the line-oriented
    interpreter interface for the AirBNB project"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """This is a quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """This method closes or terminates this session"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """This method creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            b = BaseModel()
            b.name = "ALX"
            b.save()
            print(b.id)

    def do_show(self, line):
        """This method shows the instance details
        of the given id

        Args:
            line - the argument to the command
        """
        if not line:
            print("** class name missing **")
        else:
            data = line.split()
            if data[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(data) != 2:
                print("** instance id missing **")
            else:
                fs = storage
                all_objs = fs.all()
                if f'BaseModel.{data[1]}' not in all_objs.keys():
                    print("** no instance found **")
                else:
                    for key in all_objs.keys():
                        if f'BaseModel.{data[1]}' == key:
                            b = BaseModel(**all_objs[key])
                            print(b)

    def do_destroy(self, line):
        """This method deletes an instance based on
        the class name and id

        Args:
            line - the command argument, passed.
        """
        if not line:
            print("** class name missing **")
        else:
            data = line.split()
            if data[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(data) < 2:
                print("** instance id missing **")
            else:
                fs = storage
                all_objs = fs.all()
                key = f'BaseModel.{data[1]}'
                if key not in all_objs.keys():
                    print("** no instance found **")
                else:
                    for k in all_objs.keys():
                        if k == key:
                            all_objs.pop(k)
                            break
                    for obj_dict in all_objs:
                        c = BaseModel(**all_objs[obj_dict])
                        fs.new(c)
                    fs.save()

    def do_all(self, line):
        """This method prints all string representation
        of all instances based or not on the class name

        Args:
           line - the command argument, passed.
        """
        if line and line != 'BaseModel':
            print("** class doesn't exist **")
        else:
            data = []
            fs = storage
            all_objs = fs.all()
            for value in all_objs.values():
                temp = BaseModel(**value)
                data.append(str(temp))
            print(data)

    def do_update(self, line):
        """This method updates an instance based on the class
        name and id by adding or updating attribute (save the
        change into the JSON file).

        Args:
            line - the command line argurment(s)
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif not args[1]:
                print("** instance id missing **")
            else:
                fs = storage
                all_objs = fs.all()
                key = f'BaseModel.{args[1]}'
                if key not in all_objs.keys():
                    print("** no instance found **")
                else:
                    if len(args) < 3:
                        print("** attribute name missing **")
                    elif len(args) < 4:
                        print("** value missing **")
                    else:
                        if args[3].startswith('"'):
                            args[3] = args[3][1:-1]
                        try:
                            temp = float(args[3])
                            if str(temp) == args[3]:
                                args[3] = temp
                            else:
                                temp = int(args[3])
                                if str(temp) == args[3]:
                                    args[3] = temp
                        except Exception as e:
                            pass
                        for item_dict in all_objs.values():
                            if args[1] == item_dict['id']:
                                item_dict[args[2]] = args[3]
                                d = BaseModel(**item_dict)
                                fs.new(d)
                                fs.save()
                                break


if __name__ == '__main__':
    HBNBCommand().cmdloop()
