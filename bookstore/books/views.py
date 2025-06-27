from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
import uuid
import hmac
import hashlib
import base64
from django.urls import reverse

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

# eSewa Views

import uuid
import hmac
import hashlib
import base64
from django.shortcuts import render, get_object_or_404
from .models import Book  # Adjust this import to your structure

def esewa_payment_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    tax_amount = 10
    total_amount = book.price + tax_amount

    transaction_uuid = str(uuid.uuid4())
    product_code = "EPAYTEST"  # test product code
    signed_field_names = "total_amount,transaction_uuid,product_code"

    # Must exactly match the fields and order
    signed_string = (
        f"total_amount={total_amount},"
        f"transaction_uuid={transaction_uuid},"
        f"product_code={product_code}"
    )

    # Generate signature
    secret_key ="8gBm/:&EnhH.1/q" .encode("utf-8")# eSewa test secret
    signature = base64.b64encode(
        hmac.new(secret_key, signed_string.encode("utf-8"), hashlib.sha256).digest()
    ).decode()

    context = {
        "book": book,
        "amount": book.price,
        "tax_amount": tax_amount,
        "total_amount": total_amount,
        "transaction_uuid": transaction_uuid,
        "product_code": product_code,
        "signed_field_names": signed_field_names,
        "signature": signature,
    }

    return render(request, "books/esewa_payment.html", context)


def esewa_success(request):
    return render(request, 'books/esewa_success.html')

def esewa_failure(request):
    return render(request, 'books/esewa_failure.html')
