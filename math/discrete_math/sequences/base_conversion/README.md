Conversion of an integer from base 10 to base 2 can be done by repeatedly dividing an integer by 2, and use the remainder of each division to determine the coefficients of powers.

For example, 38 can be repeatedly divided by 2 in the following way
1. $38 = 2 \times 19$ -  38 can be represented by two 19s
2. $19 = 2 \times 9 + 1$ 19 can be represented by two 9 + 1
3. $9 = 2 \times 4 + 1$ 9 can be represented by two 4 + 1
4. $4 = 2 \times 2 + 0$ 
5. $2 = 2 \times 1 + 0$
6. $1 = 2 \times 0 + 1$

The first division represents the coefficient of $2^0$, the remainder of $n^{th}$ division represents the coefficient of $2^{n-1}$. For example, 38 contains two 19s (see 1), and one 19 contains two 9s plus 1. Since 38 has two 19s, then 38 contains four 9s plus $2^1$.

The python file `base_conversion.py` converts an integer number from base 10 to base 2 with the above method. You can run it with `python3 base_conversion.py`