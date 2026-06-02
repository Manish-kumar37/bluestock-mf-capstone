-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Month

SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- 3. SIP Transactions Count

SELECT
    COUNT(*) AS sip_count
FROM investor_transactions
WHERE transaction_type = 'SIP';

-- 4. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio < 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 6. Average Return by Category

SELECT
    category,
    AVG(return_1yr_pct) AS avg_return
FROM scheme_performance
GROUP BY category;

-- 7. Top Sharpe Ratio Funds

SELECT
    scheme_name,
    sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 8. Investor Count by Gender

SELECT
    gender,
    COUNT(*) AS investors
FROM investor_transactions
GROUP BY gender;

-- 9. Total Investment Amount by Payment Mode

SELECT
    payment_mode,
    SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY payment_mode;

-- 10. Risk Grade Distribution

SELECT
    risk_grade,
    COUNT(*) AS funds
FROM scheme_performance
GROUP BY risk_grade;