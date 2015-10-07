#include <unistd.h>

int main(void) {
   execlp("login", "login", "-f", "itwenty", NULL);
}
