# Bithex #

Bithex is a Python 2 library to analyze bitcoin scripts.

# Installation #
The current release of bithex is available through pip:

    $ pip install bithex

# Quickstart #

```python
>>> import bithex
>>> bithex.compile_hex('76a914a134408afa258a50ed7a1d9817f26b63cc9002cc88ac')
'OP_DUP OP_HASH160 a134408afa258a50ed7a1d9817f26b63cc9002cc OP_EQUALVERIFY OP_CHECKSIG'
>>> bithex.classify_script('OP_DUP OP_HASH160 a134408afa258a50f26b63cc9002cc OP_EQUALVERIFY OP_CHECKSIG')
'P2PKH'
```

# Documentation #

Documentation is available at [http://bithex.readthedocs.org/en/latest/developer_interface.html](http://bithex.readthedocs.org/en/latest/developer_interface.html)

# Copyright and License #

Copyright (c) 2015 William Cember

[**Licensed**](https://github.com/wcember/bithex/blob/master/LICENSE) under the MIT License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.