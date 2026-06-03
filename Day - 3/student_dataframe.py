import pandas as pd


def create_student_df():
	data = {
		'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
		'age': [20, 21, 19, 22, 20],
		'city': ['Chennai', 'Madurai', 'Coimbatore', 'Salem', 'Tirunelveli'],
		'marks': [85, 37, 58, 42, 29],
	}
	df = pd.DataFrame(data)
	return df


if __name__ == '__main__':
	df = create_student_df()
	print('Head:')
	print(df.head())
	print('\nShape:', df.shape)
	print('\nDtypes:')
	print(df.dtypes)

	df['result'] = df['marks'].apply(lambda m: 'Pass' if m >= 40 else 'Fail')
	print("\nAfter adding 'result':")
	print(df.head())