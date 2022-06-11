//  프로그래머스 | 두 정수 사이의 합
//  https://programmers.co.kr/learn/courses/30/lessons/12912
// n ~ m 의 사이의 수 합을 구하는 수학적 정의가 있는데 이름이 생각이 안난다..
// (n+m * (|n-m|+1))/2
function solution(a, b) {
    var answer = ((a+b) * (Math.abs(a-b)+1))/2;
    return answer;
}
// console.log(solution(3,5));
