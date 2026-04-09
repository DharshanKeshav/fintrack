from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from transactions.models import Transaction, Category


class SummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        month = request.query_params.get('month')
        year = request.query_params.get('year')

        transactions = Transaction.objects.filter(user=user)

        if month and year:
            transactions = transactions.filter(
                date__month=month,
                date__year=year
            )

        total_income = transactions.filter(
            type='income'
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        total_expense = transactions.filter(
            type='expense'
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        balance = total_income - total_expense

        return Response({
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': balance,
        })


class CategoryBreakdownView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        month = request.query_params.get('month')
        year = request.query_params.get('year')

        transactions = Transaction.objects.filter(
            user=user, type='expense'
        )

        if month and year:
            transactions = transactions.filter(
                date__month=month,
                date__year=year
            )

        breakdown = (
            transactions
            .values('category__name', 'category__color')
            .annotate(total=Sum('amount'))
            .order_by('-total')
        )

        return Response(breakdown)