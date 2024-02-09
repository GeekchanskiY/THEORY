RSpec is a computer domain-specific language testing tool written in the programming language Ruby to test Ruby code. It is a behavior-driven development framework which is extensively used in production applications


```ruby
require 'rspec'

class Calculator
  def add(a, b)
    a + b
  end

  def subtract(a, b)
    a - b
  end
end

describe Calculator do
  let(:calculator) { Calculator.new }

  context "addition" do
    it "adds two numbers" do
      expect(calculator.add(2, 3)).to eq(5)
    end
  end

  context "subtraction" do
    it "subtracts two numbers" do
      expect(calculator.subtract(5, 3)).to eq(2)
    end
  end
end
```
then in shell *rspec filename.rb* to run