class Student(object):
    # def __init__(self,name):
    #     name = name
    student_num = 0

    def create_student_num(self):
        if self.student_num == 0:
            try:
                with open('student.txt', 'r')as file:
                    lines = file.readlines()
                    last_line = lines[-1]
                if last_line:
                    self.student_num = int(last_line.split(',')[0]) + 1          # '10001，小明，男，18890349090'
                else:
                    self.student_num = 10001
            except:
                self.student_num = 10001
        else:
            self.student_num += 1
        return str(self.student_num)

    def add_student_info(self,student_info):
        with open('student.txt','a') as file:
            file.write(student_info+'\n')
        return '添加成功！'

    def delete_student_info(self,student_num):
        if not self.student_exists(student_num):
            return '该学号不存在！'
        with open('student.txt','r') as file:
            lines = file.readlines()
        with open('student.txt','w') as file:
            for line in lines:
                if line[0:5] == student_num:
                    continue
                file.write(line)
        return '删除成功！'

    def edit_student_info(self,student_num):
        if not self.student_exists(student_num):
            return '该学号不存在！'
        with open('student.txt','r') as file:
            lines = file.readlines()
        with open('student.txt','w') as file:
            for line in lines:
                if line[0:5] == student_num:
                    name = input('请输入修改后的姓名：\n')
                    age = input('请输入修改后的年龄：\n')
                    gender = input('请输入修改后的性别：\n')
                    phone = input('请输入修改后的手机号码：\n')
                    student_info = ','.join([student_num,name,age,gender,phone])
                    file.write(student_info)
                else:
                    file.write(line)
            print(f'修改后的学生信息为：{student_info} \n')
        return '修改成功！'


    def get_student_info(self,student_num):
        try:
            with open('student.txt','r') as file:
                lines = file.readlines()
                for line in lines:
                    if line[0:5] == student_num:
                        result = line
                        break
                else:
                    result = '该学生的信息不存在！'
        except:
            result = '当前系统中没有录入任何学生信息！'
        return result

    def get_all_student_info(self):
        with open('student.txt','r') as file:
            result = file.read()
            return result

    def student_exists(self,student_num):
        with open('student.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                if student_num == line[0:5]:
                    return True
            else:
                return False





def show_message():
    print("学生管理系统1.0\n")
    print("请选择要进行的操作：\n")
    print("1.增加学生信息")
    print("2.删除学生信息")
    print("3.编辑学生信息")
    print("4.查询学生信息")
    print("5.查询全部学生信息")
    print("0.退出系统")


def main():
    student = Student()
    show_message()
    while True:
        try:
            number =int(input("请输入您的选择："))
        except:
            print('输入无效，请按照提示输入相应数字！')
        else:
            if number == 1:
                student_num = student.create_student_num()
                name = input('请输入学生的姓名：\n')
                age = input('请输入学生的年龄：\n')
                gender = input('请输入学生的性别：\n')
                phone = input('请输入学生的手机号码：\n')
                student_info = ','.join([student_num,name,age,gender,phone])
                result = student.add_student_info(student_info)
                print(result)
                print(f'新增的学生信息为：{student_info}')
            elif number == 2:
                student_num = input("请输入要删除的学生学号：\n")
                confirm = input('您确认要删除吗？如确认删除，请输入y/yes: \n')
                if confirm == 'y' or confirm == 'yes':
                    result = student.delete_student_info(student_num)
                    print(result)
                else:
                    print('取消删除！')
            elif number == 3:
                student_num = input("请输入要修改的学生学号：\n")
                confirm = input('您确认要修改吗？如确认，请输入y/yes：\n')
                if confirm == 'y' or confirm == 'yes':
                    result = student.edit_student_info(student_num)
                    print(result)
                else:
                    print('取消修改！')
            elif number == 4:
                student_num = input("请输入要查询的学生学号：\n")
                result = student.get_student_info(student_num)
                print(result)
            elif number == 5:
                result = student.get_all_student_info()
                print(result)
            elif number == 0:
                print("退出成功！")
                break
            else:
                print('输入无效，请按照提示输入相应数字！')





if __name__ == "__main__":
    main()