"""Эмулятор командной оболочки ОС"""
import getpass
import socket

def parse(line):
  """Разделяет строку, написанную пользователем на команды и строки
  Args:
    line - строка ввода пользователя
  Returns:
    команда + аргументы
  """
  com = []
  current = []
  q = None
  for char in line:
    if q is None:
      if char in('"', "'"):
        q = char
      elif char.isspace():
        if current:
          com.append("".join(current))
          current = []
      else:
        current.append(char)
		elif char = q:
			q = None
		else:
			current.append(char)
  if q is not None:
    raise ValueError("Unclosed quote")
  if current:
    com.append("".join(current))
  if not com:
    return None, []
  return com[0], com[1:]

def cmd_ls(args):
  """Команда заглушка команды ls, выводит аргументы"""
  return(f"ls with arguments {args}")

def cmd_cd(args):
  """Команда заглушка команды cd, выводит аргументы"""
  return(f"cd with arguments {args}")

def cmd_exit(args):
  """команда выхода из эмулятора"""
  return True

COMMANDS = {"ls":cmd_ls, "cd":cmd_cd, "exit":cmd_exit}

def prompt():
  """возвращает приглашение вида user@host:~$. """
  user = getpass.getuser()
  host = socket.gethostname()
  return f"{user}@{host}:~$. "

def prog(line):
  """Выполняет строку ввода.
  Args:
    line - строка ввода пользователя
  Returns:
    True при завершении, None иначе."""
  try:
    cmd, args = parse(line)
  except ValueError:
    print(f"parse error: {ValueError}")
    return None
  if cmd is None:
    return None
  hand = COMMANDS.get(cmd)
  if hand is None:
    print(f"Unknown command: {cmd}")
    return None
  return hand(args)

def repl():
	"""Запускает интерактивный цикл"""
	pr = prompt()
	while True:
		try:
			line = input(pr)
		except EOFError:
			break
		if prog(line):
			break

if __name__ == "__main__":
	repl()
