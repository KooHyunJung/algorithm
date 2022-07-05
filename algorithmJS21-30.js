// 프로그래머스 | k번째수
// https://programmers.co.kr/learn/courses/30/lessons/42748
// 수도코드 원본 유지, 이차 배열 commands 반복문 돌리기
function solution(array, commands) {
    var answer = [];
    for(let i = 0; i < commands.length; i++) {
        let arr = array.slice(commands[i][0]-1,commands[i][1]).sort((a,b)=>a-b);
        answer.push(arr[commands[i][2]-1])
    }
    return answer;
}
// 다른 사람 풀이 - 좀 더 직관적인듯
function solution(array, commands) {
    return commands.map(v => {
        return array.slice(v[0] - 1, v[1]).sort((a, b) => a - b).slice(v[2] - 1, v[2])[0];
    });
}
// console.log(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]));



// 프로그래머스 | 문자열을 정수로 바꾸기
// https://programmers.co.kr/learn/courses/30/lessons/12925
// Number() :  인자로 전달된 문자열을 Number 변환. 문자나 undefined 등 인자로 전달하면 NaN(Not A Number) 반환.
// parseInt() : 인자로 전달된 문자열을 Number 변환. 실수도 정수로 변환함.
function solution1(s) {
    return Number(s);
}
// console.log(solution1("1234"))



// 프로그래머스 | 문자열 다루기 기본
// https://programmers.co.kr/learn/courses/30/lessons/12918
// isNaN(value) => 'Not a Number'의 약자 문자열이 숫자인지 아닌지 판별 : 이거는 e를 숫자로 인식한다 : 4,5번 불통..
// e가 있어서 음수라서 불통.. 정규표현식 사용...
// 3번 음수에서 불통...
function solution2(s) {
    if (s.length === 4 || s.length === 6) {
        return s.includes('e') ? false : true;
    }
    return false;
}
//정규표현식 사용 통과된 풀이
function solution2(s) {
    return /^\d{4}$|^\d{6}$/.test(s)
}
console.log(solution2("e199"))
