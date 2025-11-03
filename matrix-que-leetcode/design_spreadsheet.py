def main():
    try:
        input_ = ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]
        load = [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]
        results = utility_function(input_=input_, load=load)
        print(f"Output:\t{results}")

    except Exception as e:
        print(f"Message: {e}")


def utility_function(input_ : list, load : list) -> list:
    results = [None]
    try:
        rows = load[0][0]
        sheet = [[0] * 26 for _ in range(rows)]

        def parse_term(term):
            try:
                col = ord(term[0]) - ord('A')
                row = int(term[1:]) - 1
                return row, col
            except Exception as e:
                raise Exception(f"failed to parse term: {str(e)}")

        def setCell(cell : str, value : int):
            try:
                row, col = parse_term(cell)
                sheet[row][col] = value

            except Exception as e:
                raise Exception(f"failed to set cell: {str(e)}")
        
        def resetCell(cell : str):
            try:
                row, col = parse_term(cell)
                sheet[row][col] = 0

            except Exception as e:
                raise Exception(f"failed to restset cell: {str(e)}")
            
        def getValue(formula : str):
            try:
                formula = formula[1:]
                left, right = formula.split('+')

                def get_term_value(term):
                    try:
                        term = term.strip()
                        if term[0].isalpha():
                            r, c = parse_term(term)
                            return sheet[r][c]
                        else:
                            return int(term)
                
                    except Exception as e:
                        raise Exception(f'failed to get term value: {str(e)}')
                    
                value = get_term_value(left) + get_term_value(right)
                return value

            except Exception as e:
                raise Exception(f"failed to get cell: {str(e)}")
        
        for i, action in enumerate(input_[1:], start=1):
            args = load[i]
            if action == "getValue":
                results.append(getValue(*args))
            elif action == "setCell":
                setCell(*args)
                results.append(None)
            elif action == "resetCell":
                resetCell(*args)
                results.append(None)
        return results
    except Exception as e:
        raise Exception(e)


if __name__ == "__main__":
    main()