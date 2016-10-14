/*
using UnityEngine;
using System.Collections;

public class escape : MonoBehaviour {

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
*/

﻿using UnityEngine;
using System.Collections;

namespace MLPlayer{
	public class escape : MonoBehaviour
	{
		private float speed = 2f;
		private float rotationSmooth = 1f;
		
		private Vector3 targetPosition;
		
		private float changeTargetSqrDistance = 40f;
		
		private void Start()
		{
			targetPosition = GetRandomPositionOnLevel();
		}
		
		private void Update()
		{
		// 目標地点との距離が小さければ、次のランダムな目標地点を設定する
			float sqrDistanceToTarget = Vector3.SqrMagnitude(transform.position - targetPosition);
			if (sqrDistanceToTarget < changeTargetSqrDistance)
			{
				targetPosition = GetRandomPositionOnLevel();
			}
			
		// 目標地点の方向を向く
			Quaternion targetRotation = Quaternion.LookRotation(targetPosition - transform.position);
			transform.rotation = Quaternion.Slerp(transform.rotation, targetRotation, Time.deltaTime * rotationSmooth);
			
		// 前方に進む
			transform.Translate(Vector3.forward * speed * Time.deltaTime);
		}
		
		public Vector3 GetRandomPositionOnLevel()
		{
			float levelSize = 25f;
			return new Vector3(Random.Range(-levelSize, levelSize),0,  Random.Range(-levelSize, levelSize));
		}
	}
}
