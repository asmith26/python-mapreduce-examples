This example is based the blog post: http://michaelnielsen.org/blog/write-your-first-mapreduce-program-in-20-minutes/
This computes the frequency of words in a text file(s).

#Usage

```
> cat data/text_a.txt | ./mapper.py | sort | ./reducer.py
brown   1
dogs    1
fox     1
grey    1
jumped  1
lazy    1
over    1
quick   1
the     2
```
