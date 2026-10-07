"""Тесты эмулятора"""
import uittest
from src.shell import parse, prog

class Testpars(unittest.TestCase):
  """Тесты парсера крманд"""

  def test_simple(self):
    """проверка простой команды"""
    cmd args = parse("ls lm")
    self.assertEqual(cmd, "ls")
    self.assertEqual(args, ["lm"])

  def test_multiple(self):
    """Проверка команды с несколькими аргументами"""
    cmd, args = parse("ls lm sm mm")
    self.assertEqual(cmd, "ls")
    self.assertEqual(args, ["lm", "sm", "mm"])

  def test_dquotes(self):
    """проверка обработки двойных ковычек"""
    cmd, args = parse('ls "lm sm mm"')
    self.assertEqual(cmd, "ls")
    self.assertEqual(args, ["lm sm mm"])

  def test_squotes(self):
    """Проверка обработки одинарных ковычек"""
    cmd, args = parse("ls 'lm sm mm'")
    self.assertEqual(cmd, "ls")
    self.assertEqual(args, ["lm sm mm"])

  def test_mquotes(self):
    """Проверка обработки одинарных ковычек"""
    cmd, args = parse("ls 'lm s' \"m mm\"")
    self.assertEqual(cmd, "ls")
    self.assertEqual(args, ["lm s", "m mm"])

  def test_empty(self):
    """Проверка пустой строки"""
    cmd, args = parse("")
    self.assertIsNone(cmd)
    self.assertEqual(args, [])

  def test_space(self):
    """Проверка пробела"""
    cmd, args = parse("   ")
    self.assertIsNone(cmd)
    self.assertEqual(args, [])

  def test_espace(self):
    """Проверка лишних пробелов"""
    cmd, args = parse("ls  lm    sm        mm")
    self.assertEqual(cmd, "ls")
    self.assertEqual(args, ["lm", "sm", "mm"])

  def test_err(self):
    """Проверка незакрытых ковычек"""
    with self.assertRaises(ValueError):
      parse("ls 'sm")

class Testprog(unittest.TestCase):
  """Выполнение команд"""

  def test_unknown(self):
    """Проверка неизвестной команды"""
    result = prog("sl")
    self.assertIsNone(result)

  def test_emptyy(self):
    """Проверка пустого ввода"""
    result = prog("")
    self.assertIsNone(result)

  def test_exit(self):
    """Проверка команды exit"""
    result = prog("exit")
    self.assertTrue(result)

  def test_ls(self):
    """Проверка команды ls"""
    result = prog("ls gr")
    self.assertIsNone(result)

  def test_cd(self):
    """Проверка команды cd"""
    result = prog("cd gr")
    self.assertIsNone(result)

  def test_error(self):
    """Проверка ошибки обработки"""
    result = prog("sl 'll")
    self.assertIsNone(result)

__name__ == "__main__":
unittest.main()
