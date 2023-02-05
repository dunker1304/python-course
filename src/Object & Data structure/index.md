# Python Basic

## I. String

  string[::2] -- character jumping by 2

  string[::-1] -- revert string

  string[1:4:2] -- character jump by 2 from index 1 to 4

  string * 10 -- copy string 10 times

  "string {}".format('inserted')

  "string {1} {0}".format('1', '2')

  "string {q} , {b}".format(q="asad", b="brown")

  "{value:width.precision}" -- float formating value

  f'Hello, this is {name}'

## II. List, Dictionaries, Tuples, Sets
  ```
  enumrate()
  ```

## III. I/O with basic file

  `%%writefile filename.ext`

  `with open('path/to/file', mode
      myfile.read()`

## IV. Lambda expressions: Map & Filter

  ```
    square is function, nums is array
    for item in map(square, nums):
      print(item)

    list(map(square, nums))

    square = lambda num: num**2
  ```
