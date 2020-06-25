html = b"""
<html>
    <body>
        <form method="get" action="">
        <p>
            x = <input type="number" name="x">
        </p>
        <p>
            y = <input type="number" name="y">
        </p>
        <p>  
            <input type="submit" value="Submit">
        </p>
            
        </form>
        <p>
            SUM : %(Sum)s</br>
            Product : %(Product)s</br>
        </p>
    </body>
</html>
"""