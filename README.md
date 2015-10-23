# Phrases
Generate all ordered subsets of words in a sentence.

## Usage

```python
>>> from phrases import generate_phrases
>>> list(generate_phrases("The quick brown fox"))
[
    "The",
    "The quick",
    "The quick brown",
    "The quick brown fox",
    "quick",
    "quick brown",
    "quick brown fox",
    "brown",
    "brown fox",
    "fox"
]
```
## Installation

### Using git
`git clone https://github.com/mshenfield/phrases.git`

`cd phrases`

`python setup.py install`

### Using pip
_TODO_

## License
[MIT License](http://opensource.org/licenses/MIT)
