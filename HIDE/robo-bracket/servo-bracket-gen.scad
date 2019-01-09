$fn = 40;

difference() {
	difference() {
		difference() {
			difference() {
				union() {
					translate(v = [-8, 0, 0]) {
						union() {
							linear_extrude(height = 2) {
								union() {
									union() {
										union() {
											translate(v = [2, 2, 0]) {
												offset(r = 2) {
													square(size = [4, 19]);
												}
											}
											translate(v = [4.0000000000, 11.5000000000, 0]) {
												square(size = [4.0000000000, 11.5000000000]);
											}
										}
										translate(v = [0.0000000000, 0.0000000000, 0]) {
											square(size = [4.0000000000, 11.5000000000]);
										}
									}
									translate(v = [4.0000000000, 0.0000000000, 0]) {
										square(size = [4.0000000000, 11.5000000000]);
									}
								}
							}
							translate(v = [0, 2, 0]) {
								rotate(a = [90, 0, 0]) {
									linear_extrude(height = 2) {
										union() {
											union() {
												union() {
													translate(v = [2, 2, 0]) {
														offset(r = 2) {
															square(size = [4, 20]);
														}
													}
													translate(v = [4.0000000000, 12.0000000000, 0]) {
														square(size = [4.0000000000, 12.0000000000]);
													}
												}
												translate(v = [0.0000000000, 0.0000000000, 0]) {
													square(size = [4.0000000000, 12.0000000000]);
												}
											}
											translate(v = [4.0000000000, 0.0000000000, 0]) {
												square(size = [4.0000000000, 12.0000000000]);
											}
										}
									}
								}
							}
						}
					}
					translate(v = [54.5000000000, 0, 0]) {
						mirror(v = [1, 0, 0]) {
							union() {
								linear_extrude(height = 2) {
									union() {
										union() {
											union() {
												translate(v = [2, 2, 0]) {
													offset(r = 2) {
														square(size = [4, 19]);
													}
												}
												translate(v = [4.0000000000, 11.5000000000, 0]) {
													square(size = [4.0000000000, 11.5000000000]);
												}
											}
											translate(v = [0.0000000000, 0.0000000000, 0]) {
												square(size = [4.0000000000, 11.5000000000]);
											}
										}
										translate(v = [4.0000000000, 0.0000000000, 0]) {
											square(size = [4.0000000000, 11.5000000000]);
										}
									}
								}
								translate(v = [0, 2, 0]) {
									rotate(a = [90, 0, 0]) {
										linear_extrude(height = 2) {
											union() {
												union() {
													union() {
														translate(v = [2, 2, 0]) {
															offset(r = 2) {
																square(size = [4, 20]);
															}
														}
														translate(v = [4.0000000000, 12.0000000000, 0]) {
															square(size = [4.0000000000, 12.0000000000]);
														}
													}
													translate(v = [0.0000000000, 0.0000000000, 0]) {
														square(size = [4.0000000000, 12.0000000000]);
													}
												}
												translate(v = [4.0000000000, 0.0000000000, 0]) {
													square(size = [4.0000000000, 12.0000000000]);
												}
											}
										}
									}
								}
							}
						}
					}
					difference() {
						cube(size = [46.5000000000, 33, 24]);
						translate(v = [2, 0, 2]) {
							cube(size = [42.5000000000, 31, 22]);
						}
					}
				}
				translate(v = [0, 20, 18]) {
					rotate(a = [0, 90, 0]) {
						linear_extrude(height = 46.5000000000) {
							translate(v = [3, 3, 0]) {
								offset(r = 3) {
									square(size = [4, 4]);
								}
							}
						}
					}
				}
			}
			union() {
				union() {
					translate(v = [-1, 2.1000000000, 8]) {
						rotate(a = [90, 0, 0]) {
							linear_extrude(height = 2.1000000000) {
								union() {
									union() {
										union() {
											translate(v = [0, 0]) {
												circle(r = 2.0500000000);
											}
											translate(v = [0, 10]) {
												circle(r = 2.0500000000);
											}
										}
										translate(v = [48.5000000000, 0]) {
											circle(r = 2.0500000000);
										}
									}
									translate(v = [48.5000000000, 10]) {
										circle(r = 2.0500000000);
									}
								}
							}
						}
					}
					translate(v = [0, 4, 13]) {
						union() {
							translate(v = [0, 0, -5]) {
								rotate(a = [0, 90, 0]) {
									linear_extrude(height = 46.5000000000) {
										translate(v = [-3, -2]) {
											union() {
												union() {
													translate(v = [1, 1, 0]) {
														offset(r = 1) {
															square(size = [4, 1]);
														}
													}
													translate(v = [0.0000000000, 0.0000000000, 0]) {
														square(size = [3.0000000000, 1.5000000000]);
													}
												}
												translate(v = [3.0000000000, 0.0000000000, 0]) {
													square(size = [3.0000000000, 1.5000000000]);
												}
											}
										}
									}
								}
							}
							translate(v = [0, 0, 5]) {
								rotate(a = [0, 90, 0]) {
									linear_extrude(height = 46.5000000000) {
										translate(v = [-3, -2]) {
											union() {
												union() {
													translate(v = [1, 1, 0]) {
														offset(r = 1) {
															square(size = [4, 1]);
														}
													}
													translate(v = [0.0000000000, 0.0000000000, 0]) {
														square(size = [3.0000000000, 1.5000000000]);
													}
												}
												translate(v = [3.0000000000, 0.0000000000, 0]) {
													square(size = [3.0000000000, 1.5000000000]);
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
		mirror(v = [0, 1, -1]) {
			union() {
				union() {
					translate(v = [-1, 2.1000000000, 8]) {
						rotate(a = [90, 0, 0]) {
							linear_extrude(height = 2.1000000000) {
								union() {
									union() {
										union() {
											translate(v = [0, 0]) {
												circle(r = 2.0500000000);
											}
											translate(v = [0, 10]) {
												circle(r = 2.0500000000);
											}
										}
										translate(v = [48.5000000000, 0]) {
											circle(r = 2.0500000000);
										}
									}
									translate(v = [48.5000000000, 10]) {
										circle(r = 2.0500000000);
									}
								}
							}
						}
					}
					translate(v = [0, 4, 13]) {
						union() {
							translate(v = [0, 0, -5]) {
								rotate(a = [0, 90, 0]) {
									linear_extrude(height = 46.5000000000) {
										translate(v = [-3, -2]) {
											union() {
												union() {
													translate(v = [1, 1, 0]) {
														offset(r = 1) {
															square(size = [4, 1]);
														}
													}
													translate(v = [0.0000000000, 0.0000000000, 0]) {
														square(size = [3.0000000000, 1.5000000000]);
													}
												}
												translate(v = [3.0000000000, 0.0000000000, 0]) {
													square(size = [3.0000000000, 1.5000000000]);
												}
											}
										}
									}
								}
							}
							translate(v = [0, 0, 5]) {
								rotate(a = [0, 90, 0]) {
									linear_extrude(height = 46.5000000000) {
										translate(v = [-3, -2]) {
											union() {
												union() {
													translate(v = [1, 1, 0]) {
														offset(r = 1) {
															square(size = [4, 1]);
														}
													}
													translate(v = [0.0000000000, 0.0000000000, 0]) {
														square(size = [3.0000000000, 1.5000000000]);
													}
												}
												translate(v = [3.0000000000, 0.0000000000, 0]) {
													square(size = [3.0000000000, 1.5000000000]);
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
	union() {
		translate(v = [-7, 0, 0]) {
			translate(v = [21.2500000000, 33.1000000000, 13]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.1000000000) {
						union() {
							circle(r = 4);
							union() {
								union() {
									union() {
										translate(v = [7, 0, 0]) {
											circle(r = 1.8000000000);
										}
										rotate(a = [0, 0, 90.0000000000]) {
											translate(v = [7, 0, 0]) {
												circle(r = 1.8000000000);
											}
										}
									}
									rotate(a = [0, 0, 180.0000000000]) {
										translate(v = [7, 0, 0]) {
											circle(r = 1.8000000000);
										}
									}
								}
								rotate(a = [0, 0, 270.0000000000]) {
									translate(v = [7, 0, 0]) {
										circle(r = 1.8000000000);
									}
								}
							}
						}
					}
				}
			}
		}
		translate(v = [7, 0, 0]) {
			translate(v = [21.2500000000, 33.1000000000, 13]) {
				rotate(a = [90, 0, 0]) {
					linear_extrude(height = 2.1000000000) {
						union() {
							circle(r = 4);
							union() {
								union() {
									union() {
										translate(v = [7, 0, 0]) {
											circle(r = 1.8000000000);
										}
										rotate(a = [0, 0, 90.0000000000]) {
											translate(v = [7, 0, 0]) {
												circle(r = 1.8000000000);
											}
										}
									}
									rotate(a = [0, 0, 180.0000000000]) {
										translate(v = [7, 0, 0]) {
											circle(r = 1.8000000000);
										}
									}
								}
								rotate(a = [0, 0, 270.0000000000]) {
									translate(v = [7, 0, 0]) {
										circle(r = 1.8000000000);
									}
								}
							}
						}
					}
				}
			}
		}
	}
}