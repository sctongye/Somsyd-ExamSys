from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import ast
from .models import QuestionPool, UserTestRecord, TestParams
from django.core.paginator import Paginator


class IndexView(View):
    def get(self, request):
        user_test_record = UserTestRecord.objects.all().order_by('-created')

        # 每页显示 8 篇文章
        paginator = Paginator(user_test_record, 12)

        page = request.GET.get('page')
        test_record = paginator.get_page(page)

        context = {
            'test_record':test_record,
        }
        return render(request, 'questions/main.html', context)
    def post(self, request):
        # wrong_list = request.POST.get('wrong_list')
        user_answer = request.POST.get('user_answer')
        tested_questions_list = request.POST.get('tested_questions')
        tested_questions = QuestionPool.objects.filter(pk__in=ast.literal_eval(tested_questions_list)).order_by('weighting')
        user_answer_dict = ast.literal_eval(user_answer)
        # wrong_questions = QuestionPool.objects.filter(pk__in=ast.literal_eval(wrong_list))
        context = {
            # 'wrong_questions':wrong_questions,
            'result_msg':'good',
            'showAll': True,
            'user_answer_dict': user_answer_dict,
            'tested_questions': tested_questions,
        }
        return render(request, 'questions/result2.html', context)
        # return HttpResponse(request.POST.get('wrong_list'))


class ExamPage(View):

    def get(self, request):

        # 调取设置的考试时长
        test_params = TestParams.objects.all().first()

        selected_questions = QuestionPool.objects.filter(is_active=True).order_by('weighting')

        if selected_questions:

            question_pk_list = []
            for question in selected_questions:
                question_pk_list.append(question.pk)

            context = {
                'selected_questions': selected_questions,
                'question_pk_list': question_pk_list,
                'test_params': test_params,
            }

            return render(request, 'questions/exam.html', context)

        return HttpResponse('<br><br><h2><center>No Test Currently Available</center></h2></a>')


    def post(self, request):

        user_test_record = UserTestRecord()

        user_test_record.user = request.user

        post_content = request.POST

        # print(request.POST.get('1',''))

        print(post_content)

        question_pk_list = []
        for question_pk in post_content:
            # 多选会有这种形式 '4_1': ['A'], '4_3': ['C']
            question_pk_list.append(question_pk.split('_')[0])

        # 获得了所选考题的pk列表，去掉第一个csrf token的内容
        question_pk_list = question_pk_list[1:]
        # 去重（多选会有多个重复pk
        question_pk_list = list(dict.fromkeys(question_pk_list))

        print(question_pk_list)

        # 回答列表
        user_answer_dict = {}

        # 错题列表
        wrong_list = []

        # 只要没有大段填写答案的问答题 就不改这个值 --> 不提示分值无法正确累计问题
        result_msg = 'good'

        # 总分值
        total_score = 0

        # 用户得分
        total_scored = 0

        for pk in question_pk_list:
            # print('pk值：', pk)

            question = QuestionPool.objects.get(pk=pk)

            if question.question_type == 'ss':

                # 本体分值累计
                total_score += question.score
                user_answer = request.POST.get(pk, '').lower()
                user_answer_dict[str(pk)] = user_answer

                if user_answer == question.answer.lower():
                    # print("第{0}题你选的{1}，选对了".format(pk, question.answer))
                    # 答对得分
                    total_scored += question.score
                else:
                    # print("选错了")
                    # 不得分 错分的题pk记录进错误列表
                    wrong_list.append(pk)

            if question.question_type == 'ms':

                # 本体分值累计
                total_score += question.score
                user_answer = request.POST.get(pk + '_1', '') + request.POST.get(pk + '_2', '') + request.POST.get(
                    pk + '_3', '') + request.POST.get(pk + '_4', '')
                user_answer_dict[str(pk)] = user_answer

                if user_answer.lower() == question.answer.lower():
                    # print("第{0}题你选的{1}，选对了".format(pk, question.answer))
                    # 答对得分
                    total_scored += question.score
                else:
                    # print("选错了")
                    # 不得分 错分的题pk记录进错误列表
                    wrong_list.append(pk)

            if question.question_type == 'tf':

                # 本体分值累计
                total_score += question.score
                user_answer = request.POST.get(pk, '').lower()
                user_answer_dict[str(pk)] = user_answer
                # print('user_answer: ', user_answer[:1])
                # print('question.answer: ', question.answer)
                if user_answer == question.answer.lower() or user_answer[:1] == question.answer.lower():
                    # print("第{0}题你选的{1}，选对了".format(pk, question.answer))
                    # 答对得分
                    total_scored += question.score
                else:
                    # print("选错了")
                    # 不得分 错分的题pk记录进错误列表
                    wrong_list.append(pk)

            if question.question_type == 'hand_fill_num':

                # 本体分值累计
                total_score += question.score
                user_answer = request.POST.get(pk, '').strip().lower()

                try:
                    user_answer = float(user_answer)
                    user_answer = '%g'%user_answer
                except:
                    pass

                user_answer_dict[str(pk)] = user_answer
                user_answer = str(user_answer)
                question_answer = str(question.answer).strip().lower()
                # print('user_answer: ', user_answer)
                # print('question.answer: ', question.answer)

                # 用户可能会在小数点后多加 0
                try:
                    question_answer = float(question_answer)
                    user_answer = float(user_answer)

                    print('question_answer', question_answer)
                    print('user_answer', user_answer)

                    if user_answer == question_answer:
                        total_scored += question.score
                        print('俩数都是数字且一致')

                    else:
                        print('俩数都是数字但不一致，加入错题列表')
                        wrong_list.append(pk)

                except:

                    if user_answer == question_answer:
                        # print("第{0}题你选的{1}，选对了".format(pk, question.answer))
                        # 答对得分
                        print('答案不是数字但内容一致')
                        total_scored += question.score
                    else:
                        print('答案不是数字且内容不一致')
                        # print("选错了")
                        # 不得分 错分的题pk记录进错误列表
                        wrong_list.append(pk)


            if question.question_type == 'hand_fill_answer':

                # 本体分值累计
                # total_score += question.score
                user_answer = request.POST.get(pk, '').strip().lower()
                user_answer_dict[str(pk)] = user_answer
                # print('user_answer: ', user_answer)
                # print('question.answer: ', question.answer)
                # if user_answer == question.answer.strip().lower():
                #     # print("第{0}题你选的{1}，选对了".format(pk, question.answer))
                #     # 答对得分
                #     # total_scored += question.score
                # else:
                #     # print("选错了")
                #     # 不得分 错分的题pk记录进错误列表
                #     wrong_list.append(pk)
                result_msg = ''

        user_test_record.score = total_scored
        user_test_record.total_score = total_score
        user_test_record.tested_questions = question_pk_list
        user_test_record.incorrect_question = wrong_list
        user_test_record.user_answer = user_answer_dict
        user_test_record.save()

        # 转入结果页 显示错误的题
        # 传入 错误的题 pk 以及 错误选项

        print(question_pk_list)
        # wrong_questions = QuestionPool.objects.filter(pk__in=wrong_list)
        tested_questions = QuestionPool.objects.filter(pk__in=question_pk_list).order_by('weighting')
        print(tested_questions)
        context = {
            # 'wrong_questions': wrong_questions,
            'final_score_display': str(total_scored) + ' / ' + str(total_score),
            'result_msg': result_msg,
            'user_answer_dict': user_answer_dict,
            'tested_questions':tested_questions,
        }

        return render(request, 'questions/result2.html', context)
