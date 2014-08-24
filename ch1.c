// 2. Reverse null-terminated char* str
void reverse(char* str){
	if (str){
		char * end = str;

		while(*end){
			end++; 
		}
		end--;
		char temp;
		while (str < end){
			temp = *str;
			*str++ = *end;
			*end-- = temp;
		}
	}
}


int main(){
	// char * str = "abc";
	char* str = "abcd";
	reverse(str);
	// cout << str << '\n 
}