with open('input') as f:
    _input = f.read().splitlines()

registers = {}
high = 0

def operation(condition, x, y ):
    return {
        '>': x > y,
        '<': x < y,
        '==': x == y,
        '>=': x >= y,
        '<=': x <= y,
        '!=': x != y,
    }[condition]


for line in _input:
    parts = line.split(' ')
    parts.remove('if')

    reg, action, value, x, condition, y = parts

    if reg not in registers:
        registers[reg] = 0

    if x not in registers:
        registers[x] = 0

    if operation(condition, x, y):
        if action == 'dec':
            registers[reg] += int(value)
        else:
            registers[reg] -= int(value)


print(x)

'''public static void Main()
        {
            var input = File.ReadAllLines(@"..\..\input.txt");

            var reg = new Dictionary<string, int>();
            var higest = 0;
            foreach (var line in input)
            {
                var elements = line.Split(' ');

                var regToChange = elements[0];
                var regCheck = elements[4];
                var operation = elements[1];
                var checker = elements[5];

                if(!reg.ContainsKey(regCheck))
                {
                    reg.Add(regCheck, 0);
                }

                if (!reg.ContainsKey(regToChange))
                {
                    reg.Add(regToChange, 0);
                }

                if (checker.Operator(reg[regCheck], int.Parse(elements[6])))
                {
                    if (operation == "inc")
                        reg[regToChange] += int.Parse(elements[2]);
                    else
                        reg[regToChange] -= int.Parse(elements[2]);

                    if(higest < reg[regToChange])
                        higest = reg[regToChange];
                }
            }

        }
    }

    public static class Extension
    {
        public static Boolean Operator(this string logic, int x, int y)
        {
            switch (logic)
            {
                case ">": return x > y;
                case "<": return x < y;
                case "==": return x == y;
                case ">=": return x >= y;
                case "<=": return x <= y;
                case "!=": return x != y;
                default: throw new Exception("invalid logic");
            }
        }
    }'''