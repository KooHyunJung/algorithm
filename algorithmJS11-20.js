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



// 프로그래머스 | 약수의 합
// https://programmers.co.kr/learn/courses/30/lessons/12928
function solution4(n) {
    var answer = 0;
    for (let i = 0; i < n+1; i++) {
        if (n % i === 0) answer += i;
    }
    return answer;
}
// console.log(solution4(12));



// 프로그래머스 | 두 개 뽑아 더하기
// https://programmers.co.kr/learn/courses/30/lessons/68644
function solution5(numbers) {
    const newNum = []
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            newNum.push(numbers[i] + numbers[j])
        }
    }
    const answer = [...new Set(newNum)]
    return answer.sort((a, b) => a - b)
}
// console.log(solution5([2,1,3,4,1]));



// 백준문제 | 크로아티아어
// https://www.acmicpc.net/problem/2941
// 수도코드
// 입력값과 크로아티아어 목록값 비교
// 입력값에 있는 크로아티아어는 "a"로 변경
// 문자열 길이 출력
function solution6(input) {
    let string = ['c=','c-','dz=','d-','lj','nj','s=','z='];
    for (let str of string) {
        input = input.split(str).join("a")
    }
    return input.length
}
let b = "ljes=njak"
// console.log(solution6(b))



// 구름문제 | 단어장 만들기
// https://level.goorm.io/exam/148704/%EA%B8%B0%EB%B3%B8-%EB%8B%A8%EC%96%B4%EC%9E%A5-%EB%A7%8C%EB%93%A4%EA%B8%B0/quiz/1
// 수도코드 : 배열 문자열 기준으로 오름차순 정렬, index[num-1] 찾기
function solution7(arr, num) {
    return arr.sort((x,y)=>x.length-y.length)[num-1]
}
// console.log(solution7(["a", "aa", "aaa", "b", "bb", "bbb"], 3))



// 프로그래머스 | 이상한 문자 만들기
// https://programmers.co.kr/learn/courses/30/lessons/12930
// 수도코드 
// 문자열 공백으로 나누기, 짝수 대문자/ 홀수 소문자, 변환 문자 전체 연결 출력
function solution8(s) {
    var answer2 = [];
    let s_array = s.split(" ");
    for (let i = 0; i < s_array.length; i++) {
        let answer1 = '';
        let for_array = s_array[i];
        for (let j = 0; j < for_array.length; j++) {
            if(j % 2 === 0) {
                answer1 += for_array[j].toUpperCase();
            }    
            else {
                answer1 += for_array[j].toLowerCase();
            }
        }
        answer2.push(answer1);
    }
    return answer2.join(" ");
}
// 코드 정리
function solution8(s) {
    var answer = "";

    for (let s_array of s.split(" ")) {
        for (let i = 0; i < s_array.length; i++) {
            answer +=[i % 2 ===0 ? s_array[i].toUpperCase() : s_array[i].toLowerCase()];
        }
        answer += " ";
    }

    return answer.slice(0,-1);
}
// console.log(solution8("aaa aaaa aaaaa"))
