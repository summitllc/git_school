# Important Concepts in Git
Now that you have the basic concept of what git it, and how to use it, it's time to dive into some important concept 
pertain to git and its usage, as well as some surounding topics and bits of information that need to be considered as a 
software developer on GitHub (or other platforms like it). This list will likely be a constant work in progress, as the 
authors come across questions and ideas that we did not consider at the time of this writing. Feel free to check in 
frequently to see if something new has come to our attention. Additionally, if you think of something that is not 
included, feel free to create an issue in this repo requesting that we talk about something. 

## GitHub Issues
Since we are talking about issues, why not mention it first? 

An issue on GitHub is an object to initiate work on a repo or start a conversation about future work. Often, you will 
see issues as a way of reporting bugs in a repo or to request new features in a repo. You will often see issues being 
opened by users of a repo who may not now how to fix the bug themselves. 

Once an issue is opened, the owners of the repo are notified, at which point they can engage in a conversation, by 
leaving a comment, assigning it to a particular developer, adding labels, linking it to project or milestones, or 
requesting more information from the person who opened the issue. 

## Markdown
In case you didn't notice, you're reading a Markdown file right now. Markdown is best defined as a lightweight markup 
langauge. Think of it as an easy and stripped down version of HTML. Markdown is the default method of documenting 
information and instructions about your repo on GitHub (and may other locaitons for that matter). Its primary strength 
is its simply syntax to rapidly format and organize your document. 

Some basics of Markdown include the following characters to format the text in various ways:

`#`: This symbol (pound sign, hashtag, octothorp, or whatever you want to call it) is used for the various levels of 
headers. A Single `#` will produce the HTML equivalent of `h1`. placing multiple `#` side by side will create subheaders.
The following text produces the headers displayed below
```
# Header 1
## Header 2
### Header 3
#### Header 4
```
# Header 1
## Header 2
### Header 3
#### Header 4

You can select up to 6 levels of headers, much like in HTML. 

We can also format bits of the paragraph text such as by through 
- *italicized text*: `*italicized text*`
- **boldface text**: `**boldface text**`
- `monospace text`: ``monospace text``

We create lists by using `-` or `*` for unordered lists (as demonstrated above) and numbers followed by a period for an 
ordered list (`1.`). The ordered lists would be rendered as below:
1. first item
2. second item
3. third item

One additional thing that you can include is blocks of code. The above mentioned `monospace text` is useful when 
referencing functions, files, or other small bits of logic. However, sometimes, you want to include a longer bit of code.
A code block needs to be wrapped by three (3) backtick characters (`). As an additional bonus, GitHub (and most other 
renders) can provide syntax highlighting to help readability by including the name of the language just after the first 
set of backticks. Below is an example of how it will be rendered. For the code that generates this, please review the 
raw text of the file.

```python
print("hello world")

def function_name(args1): 
    return args1[1] + 1
```

This is not all that Markdown can do, but this is only intended as an initial guide, as Markdown is the default 
documentation method for repos in GitHub. There are many types of programs that can edit and render Markdown files. 
Please look further into Markdown outside of this 

## Git Ignore
Git ignore is a file that git recognizes to exclude tracking specific files and file types. 


## Git Large File Storage (git-lfs)

## Licenses

## Git Commit History Mistakes

## GitHub Issues

