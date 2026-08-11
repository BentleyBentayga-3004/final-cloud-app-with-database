from django.contrib import admin
# Import 7 classes từ file models.py của bạn
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Khai báo các lớp Inline
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4 # Hiển thị sẵn 4 ô trống để nhập 4 đáp án (A, B, C, D)

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5 # Hiển thị sẵn 5 ô trống để nhập câu hỏi

# Nhúng Choice vào Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'course']

# Nhúng Question vào Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title', 'course']

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')

# Đăng ký các model để chúng xuất hiện trên giao diện Admin
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Choice)
admin.site.register(Submission)