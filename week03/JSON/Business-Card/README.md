BusinessCard
========

You have a `data.json` with the same people from the previous task. It's updated and has a little bit more information for each person (feel free to add more if you want). Your task is to transform the data into an HTML files so the user can open it in the browser. Create something like a `business card`. Output the name of the file in the console (or open it directly in the browser).

**NOTE 1** I've added some "avatars" in the `avatars/` directory. The names of the files are contained in `data.json`.

**NOTE 2** Don't forget to copy `styles.css` in the directory where you will generate the `.html` file. Add `<link rel="stylesheet" type="text/css" href="styles.css">` as shown in `example.html`.

**NOTE 3** Pay attention to the `class` properties in the `example.html`. We've added some default CSS styles with `styles.css`. **They match by the class property values!**

```
$ python3 business_card.py data.json
```

This should print or open HTML files for each person.

Example:
This is how the HTML file for 'Ivo Ivo' (`ivo_ivo.html`) should look like:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Ivo Ivo</title>
  <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
  <div class="business-card male">
    <h1 class="full-name">Ivo Ivo</h1>
    <img class="avatar" src="avatars/ivo.png">
    <div class="base-info">
      <p>Age: 25</p>
      <p>Birth date: 05/05/2005</p>
      <p>Birth place: Sofia</p>
      <p>Gender: male</p>
    </div>
    <div class="interests">
      <h2>Interests:</h2>
      <ul>
        <li>eating</li>
        <li>sleeping</li>
        <li>programming</li>
        <li>skiing</li>
      </ul>
    </div>
    <div class="skills">
      <h2>Skills:</h2>
      <ul>
        <li>C++ - 30</li>
        <li>PHP - 20</li>
        <li>Python - 80</li>
        <li>C# - 25</li>
      </ul>
    </div>
  </div>  
</body>
</html>
```