<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
</head>
<body>

    <h1>Add Two Numbers</h1>

    <form method="POST">
        <input type="number" name="a" placeholder="First number">
        <input type="number" name="b" placeholder="Second number">
        <button type="submit">Add</button>
    </form>

    <h2>Result: {{ result }}</h2>

</body>
</html>