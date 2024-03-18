from gradio_client import Client

if __name__ == '__main__':
	output_path = "/Users/lacri/Documents/PycharmProjects/VideoTool/facefusion/tests/test/temp"
	# client = Client("http://192.168.110.144:7860/")
	client = Client("http://127.0.0.1:7860")
	result = client.predict(
		fn_index=38
	)
	print(result)
