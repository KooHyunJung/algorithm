//  프로그래머스 | 두 정수 사이의 합
//  https://programmers.co.kr/learn/courses/30/lessons/12912
// n ~ m 의 사이의 수 합을 구하는 수학적 정의가 있는데 이름이 생각이 안난다..
// (n+m * (|n-m|+1))/2
function solution(a, b) {
    var answer = ((a+b) * (Math.abs(a-b)+1))/2;
    return answer;
}
// console.log(solution(3,5));


// 프로그래머스 | 자연수 뒤집어 배열
// https://programmers.co.kr/learn/courses/30/lessons/12932
// 변수.toString(); - 숫자를 문자열로 변환
// 배열.reverse(); - 배열 뒤집기
// 배열.map(x=>+x); - 배열의 모든 항목을 숫자로 변환
function solution1(n) {
    let re_num = n.toString();
    re_num = Array.from(re_num).reverse().map(x=>+x);
    return re_num
}
// console.log(solution1(12345));


// 프로그래머스 | 가운데 수 가져오기
// https://programmers.co.kr/learn/courses/30/lessons/12903
// Math.floor(숫자 or 연산) - 소수점 버림, 정수 반환
// 배열.slice(n,m); - n ~ m-1까지 반환
// 배열[0] - 인덱스 요소 반환
function solution2(s) {
    let s_length = s.length;
    let answer = Math.floor(s.length / 2)
    if (s_length %2 === 0) {
        return s.slice(answer-1,answer+1);
    }
    else {
        return s[answer];
    }    
}
// 삼항 연산자 사용
function solution2(s) {
    let s_length = s.length;
    let answer = Math.floor(s.length / 2)  

    return s_length %2 === 0 ? s.slice(answer-1,answer+1) : s[answer];
}
// console.log(solution2("abcd"));

