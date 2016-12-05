# ObjectComparer-in-C-Sharp
#  Created by Keith Coleman on 11/26/16.
#  Copyright © 2016 Keith Coleman. All rights reserved.
#

using System;
using System.Collections.Generic;
using System.Collections;
using System.Reflection;
using System.Text;
using System.Threading;public class CompareObjects extends object implements IComparer {
	private string methodName = "toString";
	private int SortDirection = 1;
	
	public static readonly int ASCENDING = 1;
	public static readonly int DESCENDING = -1;
	
	public CompareObjects(int SortDirection) {
		this.SortDirection = SortDirection;
	}
	
	public CompareObjects(string methodName, int SortDirection) {
		this(SortDirection);
		this.methodName = methodName;
	}
	
	public int compare(object o1, object o2) {
		object comp1 = null;
		object comp2 = null;
		try {
		Method o1_Method = o1.getClass().getMethod(methodName, null);
		Method o2_Method = o2.getClass().getMethod(methodName, null);
		comp1 = o1_Method.invoke(o1, null);
		comp2 = o2_Method.invoke(o2, null);
		
		} catch (NoSuchMethodException e) {
		} catch (IllegalAccessException e) {
		} catch (InvocationTargetException e) {}
		IComparable c1 = (IComparable) comp1;
		IComparable c2 = (IComparable) comp2;
		return c1.compareTo(c2) * SortDirection;
	}
	
	public bool equals(object obj) {
		return this.equals(obj);
	}
}
