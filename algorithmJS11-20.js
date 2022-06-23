// 프로그래머스 | x만큼 간격이 있는 n개의 숫자
// https://programmers.co.kr/learn/courses/30/lessons/12954
// 수도코드
// 반복문 돌려서 배열에 하나씩 값 추가 
function solution(x, n) {
    var answer = [];
    for (let i = 1; i < n+1; i++) {
        answer.push(x * i);
    }
    return answer;
}
// 다른 사람 풀이
function solution(x, n) {
    return Array(n).fill(x).map((v, i) => (i + 1) * v)
}
// console.log(solution(-4, 2))



// 프로그래머스 | 2016
// https://programmers.co.kr/learn/courses/30/lessons/12901
function solution1(a, b) {
    const day = ["FRI","SAT","SUN","MON","TUE","WED","THU"];
    const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    var sum = b-1;

    for (var i=0; i<a-1; i++){
        sum += month[i];
    }
    return day[(sum%7)];
}
// Date 사용
function solution1(a, b) {
    return new Date(2016, a - 1, b).toString().slice(0,3).toUpperCase();
}
// console.log(solution1(5, 24))


// 프로그래머스 | 수박
// https://programmers.co.kr/learn/courses/30/lessons/12922
// 수도코드
// arr = 수박 * n.길이
// arr.slice(0.n.길이)
function solution2(n) {
    const arr = "수박".repeat(n).slice(0,n);
    return arr;
}
// 함수를 아래처럼 쓸 수 있음
// const solution2 = n => "수박".repeat(n).slice(0,n);
// console.log(solution2(3));



// 프로그래머스 | 자릿수 더하기
// https://programmers.co.kr/learn/courses/30/lessons/12931
// 정수 -> 문자열 -> 쪼개기 -> 정수 -> SUM
function solution3(n) {
    let answer = 0;
    for (let i = 0; i < n.toString().length; i++) {
        answer += Number(n.toString()[i]);
    }
    return answer;
}
// 다른 사람 풀이
function solution3(n){
    return (n+"").split("").reduce((acc, curr) => acc + parseInt(curr), 0)
}
// console.log(solution3(123));